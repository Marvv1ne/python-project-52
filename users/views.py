from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from .models import AppUser
from django.contrib import messages
from django.shortcuts import redirect


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserForm
    success_url = reverse_lazy("home_users")
    template_name = "users/registration.html"
    #extra_context = {'title': gettext_lazy('Create user')}
    success_message = gettext_lazy('User created successfully')


class ListUsers(ListView):
    model = AppUser
    template_name = 'users/all_users.html'
    context_object_name = 'users'
    extra_context = {'title': gettext_lazy('Users')}




class UpdateUser(SuccessMessageMixin, UpdateView):
    model = AppUser
    template_name = 'users/registration.html'
    form_class = UserForm
    success_url = reverse_lazy('home_users')
    success_message = gettext_lazy('User successfully changed')


class DeleteUser(SuccessMessageMixin, DeleteView):
    model = AppUser
    success_url = reverse_lazy('home_users')
    success_message = gettext_lazy('User successfully deleted')
