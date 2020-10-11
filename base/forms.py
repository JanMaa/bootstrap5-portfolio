from django.forms import ModelForm
from . models import Message


class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'