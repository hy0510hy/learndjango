from django.db import models

# Create your models here.
class Title(models.Model):
	title_text = models.CharField(max_length=50)
	title_date = models.DateTimeField('date published')

class content(models.Model):
	content_title = models.ForeignKey(Title, on_delete=models.CASCADE)
	content_text = models.CharField(max_length=500)
	content_date = models.DateTimeField('date published')
	content_files = models.CharField(max_length=500)