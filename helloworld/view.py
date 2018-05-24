'''from django.http import HttpResponse

def hello(request):
	return HttpResponse("HelloWorld")'''
from django.shortcuts import render

def hello(request):
	context={}
	context["hello"] = "hello world"
	context["listnum"] = [1,2,3,4,5]
	return render(request,"hello.html",context)
