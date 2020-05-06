from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import PostCreateForm
from django.contrib import messages

# TODO: 現時点ではログイン必須にはしない
# @login_required(login_url='/admin/login')
def index(request):
    posts = Post.objects.all()
    params = {
        "login_user": request.user,
        "posts": posts,
        "form": PostCreateForm()
    }
    return render(request, "index.html", params)

# @login_required(login_url='/admin/login/')
def post_create(request):
    form = PostCreateForm(request.POST, instance=Post())
    if form.is_valid():
        form.save()
        print("ppp")
    else:
        print("lll")
        form = PostCreateForm
    print("KKKKK")
    return redirect(to='/post_content')

def post_content(request):
    posts = Post.objects.all()
    params = {
        "login_user": request.user,
        "posts": posts,
        "form": PostCreateForm()
    }
    return render(request, "post_create.html", params)