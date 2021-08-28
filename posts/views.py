from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
import sqlite3
from .models import *
from .forms import *
from django.contrib import messages


# from .forms import *


# Create your views here.


# conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
# cur = conn.cursor()


def index(request):
    posts = Post.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        # posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
        posts = posts.filter(Q(title__icontains=query))

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'items': posts
    }

    return render(request, 'posts/index.html', context)


def postDetail(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {
        'item': post
    }
    return render(request, 'posts/single-data.html', context)


@login_required(login_url='/admin')
def createPost(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        newData = form.save()
        messages.success(request, 'Post Successfully Created')
        return redirect('single.post', newData.id)
        # return HttpResponseRedirect(newData.get_absolute_url())

    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)


@login_required(login_url='/admin')
def postDelete(request, pk):
    data = get_object_or_404(Post, pk=pk)
    context = {
        'item': data
    }
    if request.method == 'POST':
        data.delete()
        messages.success(request, 'Post Successfully Deleted')
        return redirect('index')

    return render(request, 'posts/delete-page.html', context)


def updatePost(request, pk):
    data = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=data)

    if form.is_valid():
        form.save()
        messages.success(request, 'Post Successfully Updated')
        return redirect('single.post', data.id)

    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)
