from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('user/<int:id>', views.userdetail, name='userdetail'),
    path('like/<int:post_id>', views.like, name='like'),
]