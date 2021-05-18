from django import forms
from .models import Machine

class MachineForm(forms.ModelForm):
    PICK_USED = False
    PICK_NEW = True

    PICKS = [
        (PICK_USED, '중고 기계'),
        (PICK_NEW, '신품 기계'),
    ]

    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'post-title form-control',
                'placeholder': '제목을 입력하세요',
            }
        )
    )
    category = forms.ChoiceField(
        label='분류',
        choices= PICKS,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
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
        model = Machine
        # fields = '__all__'
        fields = ('title', 'category', 'content', 'photo',)
