from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Task
from webapp.forms import TaskForm


class TaskDetail(DetailView):
    template_name = 'task.html'
    model = Task
    context_object_name = 'tasks'


class TaskUpdateView(UpdateView):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'tasks'

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'delete.html'
    context_object_name = 'tasks'
    model = Task
    success_url = reverse_lazy('index_page')


class TaskAddView(CreateView):
    template_name = 'task_add.html'
    model = Task
    context_object_name = 'tasks'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})
