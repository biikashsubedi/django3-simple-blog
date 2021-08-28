from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('post/<str:pk>/', postDetail, name='single.post'),
    path('create/', createPost, name='create.post'),
    path('delete/<str:pk>', postDelete, name='delete.post'),
    path('update/<str:pk>', updatePost, name='update.post'),
]
