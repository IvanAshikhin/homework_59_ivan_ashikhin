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


class NotStartWithNumberValidator(BaseValidator):
    message = 'Описание не должно начинаться с цифры.'
    code = 'not_start_with_number'

    def __init__(self, limit_value=None):
        super().__init__(limit_value=limit_value)

    def validate(self, value):
        if value and value[0].isdigit():
            return self.message
        return None



class TaskForm(forms.ModelForm):
    summary = forms.CharField(validators=[MaxLengthValidator()])
    description = forms.CharField(validators=[NotStartWithNumberValidator()])

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