from django import forms
from .models import Post, Question, Answer

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'post-title form-control',
                'placeholder': '제목을 입력하세요',
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'post-content form-control',
                'placeholder': '내용을 입력하세요',
                'rows': 7,
            }
        ),
        error_messages={
            'required': '내용을 입력하세요',
        }
    )

    class Meta:
        model = Post
        fields = ('title', 'content', )

class QuestionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Question
        fields = '__all__'

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content', )
