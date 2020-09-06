from django.db import models
import uuid
import string
import random
from random import choice
from string import ascii_uppercase

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    uniqueid = models.CharField(max_length=6,null=True, blank=True, unique=True)
    password = models.CharField(max_length=100)
    rpassword = models.CharField(max_length=100)


    def save(self):
        if (not self.uniqueid):
            char="1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
            a=''.join(random.choice(char) for _ in range(6))
            self.uniqueid = a
        super(User, self).save()
