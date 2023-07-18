from django.db import models

# Create your models here.
class Post(models.Model):
    category_choices = (('일반', '일반'), ('질문', '질문'), ('후기', '후기'), ('공지', '공지'))
    category = models.CharField(max_length=30, choices = category_choices)
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.post.title}'
