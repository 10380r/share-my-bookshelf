from django.shortcuts import render
from .models import Post

# TODO: 現時点ではログイン必須にはしない
# @login_required(login_url='/admin/login')
def index(request):
    posts = Post.objects.all()
    params = {
        "login_user": request.user,
        "contents": posts,
    }
    return render(request, "index.html", params)
