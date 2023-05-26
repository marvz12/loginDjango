from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin, name="userLogin"),
    path('profile', views.home, name="profile"),
    path('register/', views.register_user, name="register"),
    
]