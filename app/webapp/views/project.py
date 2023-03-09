from django.views.generic import ListView, DetailView, CreateView

from webapp.models.project import Project

from webapp.models import Task


class ProjectsIndexView(ListView):
    template_name = 'project_index.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetail(DetailView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['tasks'] = Task.objects.filter(project=project.pk)
        return context


class AddProject(CreateView):
    template_name = 'task_add.html'
    model = Task
    context_object_name = 'tasks'
    form_class = TaskForm