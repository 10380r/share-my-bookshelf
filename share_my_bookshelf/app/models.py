from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=1000, default="")
    label = models.CharField(default=None, max_length=15)
    star = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    isbn_code = models.CharField(default="0000000000000", max_length=13)
    title = models.TextField(default="")
    subtitle = models.TextField(default="")
    authors = models.TextField(default="")
    published_date = models.CharField(default=None, max_length=8)
    description = models.TextField(default="")
    img_url = models.TextField(default="")
    was_read = models.BooleanField(default=False)

    def __str__(self):
        return "%s (Post ID: %s)" % (self.username, self.id)

    class Asc_date:
        # - にしておくと昇順で表示
        ordering = ("-published_date",)


class Friend(models.Model):
    myself = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friend_myself"
    )
    friend = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%s)" % (self.friend)
