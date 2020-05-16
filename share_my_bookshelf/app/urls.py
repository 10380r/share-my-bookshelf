from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    #path('post_content', views.post_content, name='post_content'),
]
