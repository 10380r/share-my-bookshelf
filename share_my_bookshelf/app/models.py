from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=1000, default="")
    label = models.CharField(default=None, max_length=15)
    star = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    isbn_code = models.CharField(default="0000000000000", max_length=13)
    title = models.TextField(default="")
    subtitle = models.TextField(default="", blank=True)
    authors = models.TextField(default="")
    published_date = models.CharField(default=None, max_length=10)
    description = models.TextField(default="")
    img_url = models.TextField(default="")
    was_read = models.BooleanField(default=False)

    def __str__(self):
        return '%s (PostID: %s)' %(self.username, self.id)

    class Asc_date:
        # - にしておくと昇順で表示
        ordering = ('-pub_date',)


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="like_owner")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
