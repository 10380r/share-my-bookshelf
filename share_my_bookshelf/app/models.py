from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    username    = models.ForeignKey(User, on_delete=models.CASCADE, \
                  related_name = 'post_username')
    post_date   = models.DateTimeField(auto_now_add=True)
    isbn_code   = models.TextField(max_length=13, default="")
    author      = models.TextField(default="")
    title       = models.TextField(default="")
    review      = models.TextField(max_length=1000, default="")
    label       = models.CharField(default=None, max_length=15)
    star        = models.IntegerField(default=0)
    like        = models.IntegerField(default=0)

    def __str__(self):
        return '%s (written by: %s)' %(self.title, self.author)

    class Asc_date:
        # - にしておくと昇順で表示
        ordering = ('-pub_date',)

class Friend(models.Model):
    myself      = models.ForeignKey(User, on_delete=models.CASCADE,\
                  related_name='friend_myself')
    friend      = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' %(self.friend)

        # change tomiyama
