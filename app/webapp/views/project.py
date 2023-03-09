from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.models.project import Project
from webapp.models import Task

from webapp.forms import ProjectForm


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


class AddProjectView(CreateView):
    template_name = 'project_add.html'
    model = Project
    context_object_name = 'projects'
    form_class = ProjectForm


    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
