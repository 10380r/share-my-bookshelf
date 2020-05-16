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
def post(request):
    params = {}
    if request.method == 'POST':
        post = Post()
        post.username = request.user
        post.review =  request.POST['review']
        post.label =  request.POST['label']
        post.star =  request.POST['star']
        post.isbn_code = request.POST['isbn_code']
        post.publishedDate = request.POST['publishedDate']
        post.save()
        return redirect(to='/')

    else:
        form = PostCreateForm()
        params['form'] = form
        return render(request, 'post_create.html', params)
