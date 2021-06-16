from django import forms
from .models import Post, Question, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Question
        fields = '__all__'

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content', )
