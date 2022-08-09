from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logOn/', views.log_on, name='logon'),
    path('logOut/', views.log_out, name='logout')
]
