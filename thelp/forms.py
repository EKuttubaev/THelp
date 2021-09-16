from django.forms import ModelForm
from django import forms

from thelp.models import Task, Comment


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ["status_done", "ip_adress"]
        widgets = {
            "appeal": forms.Textarea(attrs={'placeholder': 'Пример: Не работает принтер'}),
            "room": forms.TextInput(attrs={'placeholder': '101'}),
            "person": forms.TextInput(attrs={'placeholder': 'ФИО сотрудника'})

        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
