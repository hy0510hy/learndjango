from django.urls import path
from .import views
#app name 指明polls的命名空间
app_name = 'knowledge'
urlpatterns = [
	path('knowledge/',views.knowledge,name='knowledge'),
	path('add',views.add,name='add'),
	path('addform/',views.addforms,name='addform'),
	path('contentajax',views.ajaxclick,name='contentajax'),
	path('downfile',views.downloadpycode,name='downfile'),
	#path(r'<int:question_id>/', views.detail, name='detail'),
	#path(r'<int:question_id>/vote/', views.vote, name='vote'),
]