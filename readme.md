# Django

install pipenv 

pipenv shell

pipenv install django

django-admin startproject <project-name>

manage.py main()


start server
python manage.py migrate

migration :
python manage.py migrate


create app :

python manage.py startapp <app-name>

make migrations:
python manage.py makemigrations <app-name>

cli-tool for manipulate data
python manage.py shell
  from polls.models import Question,Choice
   from django.utils import timezone
   Question.objects.all()
   q= Question('question_text',publish_date=timezone.now())
   q.save()
   Question.objects.filter(id=1)
   Question.objects.get(pk=1)
   q.choice_set.all()
   q.choice_set.create(choice_text="choice1",votes=0)
   

create super user : python manage.py createsuperuser