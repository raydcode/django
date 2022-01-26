
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


# Create your views here.

from .models import Question,Choice



# Get questions 

def  index(request):
    latest_questions_list = Question.objects.order_by('-publish_date')[:5]
    context = {'latest_question_list':latest_questions_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    try:
       question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn not exist")   
    return render(request,'polls/detail.html',{'question':question})


def result(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/result.html',{'question':question})


# Vote for a question choice
def vote(request, question_id):
  
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
     
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))