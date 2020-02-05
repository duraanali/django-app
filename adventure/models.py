from django.db import models

# Create your models here.
class Player(models.model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)


class Rooms(models.model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)


class Items(models.model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)