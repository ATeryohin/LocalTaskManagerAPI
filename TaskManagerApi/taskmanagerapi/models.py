import datetime

from django.db import models

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    board_id = models.IntegerField()
    def __str__(self):
        return self.name


class Card(models.Model):
    state_id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    board_id = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.title