from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)
    address = models.TextField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return (f"my name is {self.name} with phone number {self.phone} and my address is {self.address}")
