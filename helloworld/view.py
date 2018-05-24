'''from django.http import HttpResponse

def hello(request):
	return HttpResponse("HelloWorld")'''
from django.shortcuts import render

def hello(request):
	context={}
	context["hello"] = "hello world"
	return render(request,"hello.html",context)
