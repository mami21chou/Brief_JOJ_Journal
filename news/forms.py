from django import forms
from .models import Commentaire
from django.contrib.auth.forms import AuthenticationForm

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Votre commentaire...',
                'rows': 3
            })
        }
        

class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'