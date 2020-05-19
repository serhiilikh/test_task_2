from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    text = models.TextField(blank=False)
    author = models.CharField(blank=True, default="Anonymous", max_length=150)
    created = models.DateTimeField(editable=False, blank=True, null=True)


class Upvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def create(cls, post, user):
        cls.objects.get_or_create(post=post, user=user)
        return "created"
