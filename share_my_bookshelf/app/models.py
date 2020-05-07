from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    isbn_code = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=1000, default="")
    label = models.CharField(default=None, max_length=15)
    star = models.IntegerField(default=0)
    like = models.IntegerField(default=0)

    def __str__(self):
        return "%s (Post ID: %s)" % (self.username, self.id)

    class Asc_date:
        # - にしておくと昇順で表示
        ordering = ("-pub_date",)


class Book(models.Model):
    isbn_code = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    author = models.TextField(default="")
    title = models.TextField(default="")


class Friend(models.Model):
    myself = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friend_myself"
    )
    friend = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%s)" % (self.friend)
