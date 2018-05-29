from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from django.http import Http404
# Create your views here.

def savequestion(request):
	q = Question(question_text="What's new?",pub_date=timezone.now())
	q.save()
	return HttpResponse("hello,you're at the polls save question and save 1 question on mysql")

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ','.join([q.question_text for q in latest_question_list])
	return render(request,'polls/index.html',{'output':latest_question_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question.question_text})
