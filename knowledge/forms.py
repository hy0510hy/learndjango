from django import forms

class contentAdd(forms.Form):
	title = forms.CharField(label='标题',max_length=50)
	content = forms.CharField(widget=forms.Textarea(),label='内容',max_length=500)
	codefile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
	#test = forms.CharField(label='测试',max_length=20)