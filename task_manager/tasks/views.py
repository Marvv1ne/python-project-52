from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView

from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from task_manager.users.models import AppUser
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter


class TasksListView(AuthRequiredMixin, FilterView):

    template_name = 'tasks/tasks.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show'),
    }


class TaskDetailView(AuthRequiredMixin, DetailView):

    template_name = 'tasks/task_show.html'
    model = Task
    context_object_name = 'task'
    extra_context = {
        'title': _('Task preview')
    }


class TaskCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')
    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):

        user = self.request.user
        form.instance.author = AppUser.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):

    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully changed')
    extra_context = {
        'title': _('Task change'),
        'button_text': _('Change'),
    }


class TaskDeleteView(AuthRequiredMixin, AuthorDeletionMixin,
                     SuccessMessageMixin, DeleteView):

    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
    author_message = _('The task can be deleted only by its author')
    author_url = reverse_lazy('tasks')
    extra_context = {
        'title': _('Delete task'),
        'button_text': _('Yes, delete'),
    }
