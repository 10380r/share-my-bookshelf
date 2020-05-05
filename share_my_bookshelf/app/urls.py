from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post-create/', views.PostCreateView.as_view(), name='post_create'),
]
