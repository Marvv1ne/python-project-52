from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm
from .models import AppUser
from task_manager.mixins import AuthRequiredMixin, UserPermissionMixin, DeleteProtectionMixin


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserForm
    success_url = reverse_lazy("signin")
    template_name = "users/registration.html"
    #extra_context = {'title': _('Create user')}
    success_message = _('User created successfully')


class ListUsers(ListView):
    model = AppUser
    template_name = 'users/all_users.html'
    context_object_name = 'users'
    extra_context = {'title': _('Users')}


class UpdateUser(AuthRequiredMixin, UserPermissionMixin, SuccessMessageMixin, UpdateView):
    model = AppUser
    template_name = 'users/registration.html'
    form_class = UserForm
    success_url = reverse_lazy('home_users')
    success_message = _('User is successfully updated')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('home_users')
    extra_context = {
        'title': _('Update user'),
        'button_text': _('Update'),
    }


class DeleteUser(AuthRequiredMixin, UserPermissionMixin, SuccessMessageMixin, DeleteView):
    model = AppUser
    success_url = reverse_lazy('home_users')
    success_message = _('User successfully deleted')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('home_users')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('home_users')
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }
