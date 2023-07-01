from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=156)
    logo = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return str(self.name)