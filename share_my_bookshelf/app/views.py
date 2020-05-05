from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Post
from .form import PostCreateForm

# TODO: 現時点ではログイン必須にはしない
# @login_required(login_url='/admin/login')
def index(request):
    posts = Post.objects.all()
    params = {
        "login_user": request.user,
        "contents": posts,
    }
    return render(request, "index.html", params)

class PostCreateView(LoginRequiredMixin, generic.FormView):
    model = Post
    template_name = 'post_create.html'
    #フォームクラスのオーバーライド
    form_class = PostCreateForm
    #正常に処理が完了した際の遷移先の設定→リストに移動
    # success url = reverse_lazy('post:post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        massages.success(self.request, '投稿作成')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '投稿作成失敗')
        return super().form_invalid(form)