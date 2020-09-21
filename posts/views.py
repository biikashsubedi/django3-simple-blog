from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from posts.models import Post
from .forms import *


def index(requests):
    post_list = Post.objects.all().order_by('-id')
    query = requests.GET.get('q')
    if query:
        post_list=post_list.filter(Q(title__icontains=query)|Q(content__icontains=query))

    paginator = Paginator(post_list, 3)
    page = requests.GET.get('page')
    post_list = paginator.get_page(page)
    context = {
        'posts': post_list
    }
    return render(requests, 'posts/index.html', context)


def blog_detail(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)


@login_required(login_url='index')
def create_form(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Successfully Created!')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)


@login_required(login_url='index')
def blog_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, 'Successfully Deleted!')
    return HttpResponseRedirect('/')


@login_required(login_url='index')
def blog_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Updated!')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)
