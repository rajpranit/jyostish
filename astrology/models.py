from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=64,null=True)
    email = models.EmailField(max_length=64,null=True)
    subject = models.CharField(max_length=64,null=True)
    message = models.TextField(max_length=64,null=True)
   

    def __str__(self):
        return f"{self.name}"
