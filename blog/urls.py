"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import *
from users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('', index, name='index'),
                  path('detail/<int:id>', blog_detail, name='detail'),
                  path('create/', create_form, name='create'),
                  path('delete/<int:id>', blog_delete, name='delete'),
                  path('update/<int:id>', blog_update, name='update'),
                  path('login/', login_view, name='login'),
                  path('signup/', user_signup, name='signup'),
                  path('logout/', user_logout, name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
