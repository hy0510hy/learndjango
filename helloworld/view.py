'''from django.http import HttpResponse

def hello(request):
	return HttpResponse("HelloWorld")'''
from django.shortcuts import render
from django.contrib.auth.models import User
import django
def hello(request):
	data = "[{title: '苹果公司',type: 'folder',products: [{title: 'iPhone',type: 'item'},{title: 'iMac',type: 'item'},{title: 'MacBook Pro',type: 'item'}]},{ title: '微软公司',type: 'item'},{title: 'GitHub',type: 'item',attr: {icon: 'am-icon-github'}}]"
	context={}
	context["hello"] = "welcome to hello page"
	context["listnum"] = [1,2,3,4,5]
	context["data"] = data
	#切片操作
	L = ["b0","b1","b2","b3","b4","b5","b6","b7","b8","b9"]
	#0是从第一个元素开始，可以省略切到第7个元素 2是每2个元素娶一个
	context["cut"] = L[0:7:2]

	return render(request,"hello.html",context)

def landing(request):
	context={}
	context["brand"] = "hyWeb Home"
	return render(request,"landing.html",context)
'''
func[1] 等价于 func2() 的执行结果，
func2的功能是“仅在调用过程中print一次字符串`func2` ”，
在构造列表的时候，就是那次调用，故而有打印。列表构造完毕，
则列表内直接存放的函数的返回值，这三个的返回值都是None，
故而第28行等价于  None ，仅此而已，你要啥输出？
'''
def func1(p):
	string = "".join("meeetasssootaaaa")
	string1=list(set(string))
	output = "".join(string1)
	print(output)

def func2():
	print("func2")
	return "func2"

def func3():
	print("func3")

L = ["b0","b1","b2","b3","b4","b5","b6","b7","b8","b9"]
func = [func1("hi"),func2(),func3()]
print(func[1])
output = '*'.join([l for l in L])
print(output)
x,y,z = func
print(x,y,z)
print(django.get_version())
