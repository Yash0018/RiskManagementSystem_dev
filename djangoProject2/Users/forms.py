from django import forms
from .models import User, Document


class LogInForm(forms.ModelForm):
    class Meta:
        model = User

        widgets = {
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Enter Password here',
                       'type': 'password',
                       'id': 'inputPassword',
                       'class': 'form-control item'}),
            'username': forms.TextInput(
                attrs={'placeholder': 'Enter description here',
                       'type': "text",
                       'id': "inputusername",
                       'class': "form-control item",
                       }),
        }
        fields = '__all__'


class Clientdoc(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_name', 'path', 'event_id']
