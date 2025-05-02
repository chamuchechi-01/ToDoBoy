from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']  

class TaskStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('done', 'Done'),
        ('not_done', 'Not Done'),
        ('in_work', 'In Work'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES)
