from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from .models import User
from django.contrib import messages
from django.shortcuts import redirect


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserForm
    success_url = reverse_lazy("login")
    template_name = "users/registration.html"
    #extra_context = {'title': gettext_lazy('Create user')}
    success_message = gettext_lazy('User created successfully')


class ListUsers(ListView):
    model = User
    context_object_name = 'users'
    extra_context = {'title': gettext_lazy('Users')}




class UpdateUser(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('home_users')
    success_message = gettext_lazy('User successfully changed')


class DeleteUser(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home_users')
    success_message = gettext_lazy('User successfully deleted')
