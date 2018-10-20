from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=0)
    vote_total = models.IntegerField(default=1)

