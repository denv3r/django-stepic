from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField()
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.models.IntegerField()
	author = models.ForeignKey(User, on_delete=models.SET_NULL)
	likes = ManyToManyField(User)

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, on_delete=models.SET_NULL)
	author = models.ForeignKey(Question, on_delete=models.SET_NULL)