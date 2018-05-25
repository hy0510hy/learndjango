'''from django.http import HttpResponse

def hello(request):
	return HttpResponse("HelloWorld")'''
from django.shortcuts import render

def hello(request):
	context={}
	context["hello"] = "hello world"
	context["listnum"] = [1,2,3,4,5]
	#切片操作
	L = ["b0","b1","b2","b3","b4","b5","b6","b7","b8","b9"]
	#0是从第一个元素开始，可以省略切到第7个元素 2是每2个元素娶一个
	context["cut"] = L[0:7:2]

	return render(request,"hello.html",context)
