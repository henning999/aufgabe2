from django.db import models

# Create your models here.


class Todo(models.Model):
    description = models.CharField(max_length=160)
    deadline = models.DateTimeField('deadline')
    done = models.FloatField(default=0.0)
