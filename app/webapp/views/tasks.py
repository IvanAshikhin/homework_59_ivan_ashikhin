from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView

from webapp.models import Task

from webapp.forms import TaskForm


class TaskDetail(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = TaskForm(instance=context['tasks'])
        return context

    def post(self, request, *args, **kwargs):
        tasks = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            tasks.edit_time = datetime.now()
            tasks.save()
            form.save()
            return redirect('detail_task', pk=tasks.pk)
        return render(request, 'task_update.html', context={'form': form, 'tasks': tasks})


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.type.clear()
        task.delete()
        return redirect('index_page')


class TaskAddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_add.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return redirect('detail_task', pk=task.pk)
        return render(request, 'task_add.html', {'form': form})
