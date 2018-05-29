from django.urls import path
from .import views
#app name 指明polls的命名空间
app_name = 'polls'
urlpatterns = [
	path('',views.savequestion,name='svaequestion'),
	path('index/',views.index,name='index'),
	path(r'<int:question_id>/', views.detail, name='detail'),
	#path(r'<int:question_id>/vote/', views.vote, name='vote'),
]