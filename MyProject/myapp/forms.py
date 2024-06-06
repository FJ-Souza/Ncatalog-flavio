from django import forms
from django.forms import ModelForm
from myapp.models import *

class RoupaForm(forms.ModelForm):
    class Meta:

        model = Roupa
        fields = "__all__"
        labels = {
            "titulo": "titulo",
            "path": "imagem",
            "descricao": "descrição",
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome da roupa",
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
        }