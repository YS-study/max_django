from django import forms
from .models import Machine

class MachineForm(forms.ModelForm):

    PICK_USED = False
    PICK_NEW = True

    PICKS = [
        (PICK_USED, 'USED'),
        (PICK_NEW, 'NEW'),
    ]

    pick = forms.ChoiceField(choices=PICKS)
    class Meta:
        model = Machine
        fields = ('title', 'content', 'photo',)
