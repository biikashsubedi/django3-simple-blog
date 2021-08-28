from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('logout/', logoutView, name='logout'),
]
