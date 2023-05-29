from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(maxfield=256)
    password=models.passwordfield(maxfield=256)
    email=models.EmailField(maxfield=256)
    def __str__(self):
        return self.username
