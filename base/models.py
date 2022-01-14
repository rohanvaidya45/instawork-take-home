from django.db import models
from django.core.validators import RegexValidator;

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, validators=[RegexValidator(regex=r'^\d{3}-\d{3}-\d{4}$')])
    email = models.EmailField(max_length=100)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name