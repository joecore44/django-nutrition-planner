from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
        upload_to='customer_media/profile')
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name