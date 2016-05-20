from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='author_set')
	likes = models.ManyToManyField(User, related_name='likes_set')

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL, related_name='question_set')
	author = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL, related_name='author_set')