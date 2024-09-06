from django.db import models

class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    birthDate = models.CharField(max_length=255)
    birthCity = models.CharField(max_length=255)

class Books(models.Model):
    title = models.CharField(max_length=255)
    descr = models.TextField()
    genre = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

class AuthorsBooks(models.Model):
    Authors_name = models.CharField(max_length=255)
    Books_title = models.CharField(max_length=255)
