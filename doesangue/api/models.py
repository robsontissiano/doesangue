from django.db import models


class Donor(models.Model):
    name = models.CharField(max_length=120, help_text='title of donor.')
    email = models.CharField(max_length=255)
    blood = models.CharField(max_length=2)

def __str__(self):
    return self.name
