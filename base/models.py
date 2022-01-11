from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name