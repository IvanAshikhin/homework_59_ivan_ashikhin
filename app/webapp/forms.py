from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

from .models import Task


class MaxLengthValidator(BaseValidator):
    def __init__(self, limit_value=100):
        message = ('Максимальная длинна не может быть больше %(limit_value)s знаков.')
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return limit_value <= len(value)



class TaskForm(forms.ModelForm):
    summary = forms.CharField(validators=[MaxLengthValidator()])
    description = forms.CharField()

    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status']
        labels = {
            'summary': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип задачи'

        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Find')
