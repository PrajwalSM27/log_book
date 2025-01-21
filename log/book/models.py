from django.db import models

# Create your models here.
class Contact(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField()
    date=models.DateField()

    def __str__(self):
             return self.title