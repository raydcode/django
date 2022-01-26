from django.contrib import admin

# Register your models here.

from .models import Question,Choice

admin.site.site_header = "Raydcode"
admin.site.site_title = "Raydcode"
admin.site.index_title = "Raydcode"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldssets = [(None,{'fields':['question_text']}),('Date_information',{'fields':['publish_date'],'classes':['collapse']}),]
    inlines = [ChoiceInline]



admin.site.register(Question,QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)