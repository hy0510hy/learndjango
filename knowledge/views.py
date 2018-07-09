from django.shortcuts import render
from django.http import HttpResponse
from .models import Title
from .models import content
from django.utils import timezone
from django.http import Http404
from .forms import contentAdd
from django.core import files
import datetime
import json
from django.http import FileResponse


# Create your views here.
def knowledge(request):
	title_list = Title.objects.order_by('title_date')
	#print(type(title_list))
	#for t in title_list:
		#print(t.title_date)
	#	t.title_date = t.title_date.strftime('%Y%m%d')
	return render(request,'knowledge/knowledge.html',{'output':title_list})

def ajaxclick(request):
	data = request.POST
	li = data['text'];
	keyid = li.split(',')[1]
	tt = Title.objects.get(id=keyid)
	cc = content.objects.get(content_title=keyid)
	return HttpResponse(json.dumps(cc.content_text+'&'+tt.title_text+'&y'+'&'+cc.content_files),content_type='application/json; charset=utf-8')
	#return render(request,'knowledge/knowledge.html',{'cc':cc)

def add(request):
	return render(request,'knowledge/add.html')

def downloadpycode(request):
	data = request.GET.get("text")
	adir = str(data)
	print(adir)
	file = open(adir,'rb')
	l = data.split("_")
	response =FileResponse(file)
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename='+l[-1]
	return response

def addforms(request):
	if request.method=='POST':
		form = contentAdd(request.POST,request.FILES)
		print(form.errors)
		if form.is_valid():
			#print('into valid')
			datenow = timezone.localtime()
			#print(datenow)
			form_title = form.cleaned_data['title']
			form_content = form.cleaned_data['content']
			sql_title = Title(title_text=form_title,title_date=datenow)
			sql_title.save()
			key = sql_title.title_text+'_'+str(datenow).split(' ')[0]+'_'
			dirs = []
			for i in request.FILES.getlist('codefile'):
				path = 'static/pythoncodeuploadfile/'+key+str(i)
				dirs.append(path)
				handle_uploaded_file(path,i)
			j = "|"
			sql_content = content(content_title=sql_title,content_text=form_content,content_date=datenow,content_files=j.join(dirs))
			sql_content.save()
			
			#if request.FILES['codefile']!='':
			title_list = Title.objects.order_by('title_date')
			return render(request,'knowledge/knowledge.html',{'output':title_list})
		else:
			print('error valid')
	else:
		print('into init')
		form = contentAdd()
	return render(request,'knowledge/add.html',{'form':form})

def handle_uploaded_file(path,i):
	with open(path, 'wb+') as destination:
		for chunk in i.chunks():
			destination.write(chunk)
