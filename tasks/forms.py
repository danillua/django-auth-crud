from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description', 
            'important',
        ]
        labels = {
            'title' : 'Título',
            'description' : 'Descripción',
            'important':'Importante',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un título'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba una descripción'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }