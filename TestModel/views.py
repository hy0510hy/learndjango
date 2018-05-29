from django.shortcuts import render
from django.http import Http404
# Create your views here.
from .models import Test

def detail(request,nameid):
	try:
		name = Test.objects.get(pk=nameid)
	except Test.DoesNoteExist:
		raise Http404("Test does not exist")
	return render(request,'detail/detail.html',{'rname':name})