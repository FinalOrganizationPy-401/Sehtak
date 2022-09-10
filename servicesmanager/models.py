from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.


class Medicine(models.Model):
    """
    Midicine model

    """

    names = models.CharField(max_length=255, blank=True)
    doses = models.IntegerField(blank=True)
    add_date = models.DateField(auto_now_add=True)
    result_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.names


class Tests(models.Model):
    """
    Tests model

    """

    names = models.CharField(max_length=255, blank=True)
    add_date = models.DateField(auto_now_add=True)
    result_date = models.DateField(auto_now=True)
    folder_url = models.CharField(max_length=255, blank=True)


class X_Rays(models.Model):
    """
    X_Rays Model
    """

    names = models.CharField(max_length=255, blank=True)
    add_date = models.DateField(auto_now_add=True)
    result_date = models.DateField(auto_now=True)
    folder_url = models.CharField(max_length=255, blank=True)
