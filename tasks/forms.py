from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'título': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un título'}),
            'descripción': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba una descripción'}),
            'importante': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }