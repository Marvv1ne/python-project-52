from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('registration/', views.UserRegisterView1.as_view(), name='registration'),
    path('<int:user_id>/', views.get_user_info, name='user_info'),
]