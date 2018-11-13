from django.db import models

# Create your models here.
class mainmenu(models.Model):
    idd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)


class submenu(models.Model):
    idd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)


class contact(models.Model):
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    message = models.CharField(max_length=30)