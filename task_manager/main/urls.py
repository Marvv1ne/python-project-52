
from django.urls import path
from . import views


urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
   path('signin/', views.UserLoginView.as_view(), name='signin'),
   path('signout/', views.UserLogoutView.as_view(), name='signout'),
]
