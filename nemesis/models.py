from django.db import models

# Create your models here.
class Sign(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=12)
    confirmpassword = models.CharField(max_length=12)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.username