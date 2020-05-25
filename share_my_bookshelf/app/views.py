import json
from itertools import groupby

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import CustomUser

from .forms import PostCreateForm
from .models import Like, Post
from .util.inquire_book_info import request_googleapi


@login_required(login_url="/accounts/login/")
def index(request):
    posts = Post.objects.all()
    params = {
        "login_user": request.user,
        "posts": posts,
    }
    return render(request, "index.html", params)


@login_required(login_url="/accounts/login/")
def post(request):
    params = {}
    if request.method == "POST":
        post = Post()
        post.username = request.user
        post.isbn_code = request.POST["isbn_code"]
        book_info = request_googleapi("", "", post.isbn_code)
        post.title = book_info["title"]
        post.subtitle = book_info["subtitle"]
        post.authors = ",".join(book_info["authors"])
        post.published_date = book_info["published_date"]
        post.description = book_info["description"]
        post.img_url = book_info["image_url"]
        post.review = request.POST["review"]
        post.label = request.POST["label"]
        post.star = request.POST["star"]
        post.save()
        return redirect(to="/")

    else:
        form = PostCreateForm()
        params["form"] = form
        return render(request, "post_create.html", params)


@login_required(login_url="/accounts/login/")
def userdetail(request, id):
    posts = Post.objects.all()

    user = CustomUser.objects.get(id=id)

    filtered = list(filter(lambda post: post.username.id == id, posts))

    # list<str>
    labels_names = list(map(lambda post: post.label, posts))
    labels_count = list(map(lambda label: labels_names.count(label), labels_names))

    # ジャンル:個数 の辞書を作成する
    # JSに渡すことを想定しているので同時にjsonに変換
    labels_json = json.dumps(
        {label: count for label, count in zip(labels_names, labels_count)}
    )

    params = {
        "login_user": request.user,
        "user": user,
        "posts": filtered,
        "labels_json": labels_json,
    }

    return render(request, "userpage.html", params)


@login_required(login_url="/accounts/login/")
def like(request, post_id):
    post = Post.objects.get(id=post_id)
    is_like = Like.objects.filter(user=request.user).filter(post=post).count()

    # いいね済みの場合はカウントしない
    if is_like > 0:
        return redirect(to="/")

    # いいねカウント
    post.like_count += 1
    post.save()

    like = Like()
    like.user = request.user
    like.post = post
    like.save()

    return redirect(to="/")
