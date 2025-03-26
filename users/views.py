from django.views.generic.edit import CreateView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import User
from .forms import UserRegisterForm

def get_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/all_users.html', context)


def get_user_info(request, user_id):
    user = User.objects.filter(pk=user_id)
    context = {'user_info': user}
    return render(request, 'users/user_info', context)

class UserRegisterView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegisterForm
    success_url = '/users/' # или reverse_lazy('users')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['user_info'] = User.objects.all() #необходимо ли?
        return context

class UserRegisterView1(View):
    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'users/registration.html', {'form': form})



