from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'taskInput',
                'placeholder': 'Название задания'
            }),
            "task": Textarea(attrs={
                'class': 'taskArea',
                'placeholder': 'Описание задания'
            })
        }