from django.db import models

# Create your models here.
class users(models.Model):
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.firstName} {self.secondName} ({self.age})"
   
