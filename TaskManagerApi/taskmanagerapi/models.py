import datetime

from django.db import models

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title