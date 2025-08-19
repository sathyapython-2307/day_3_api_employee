# ...existing code...
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    head = models.ForeignKey('Employee', null=True, blank=True, on_delete=models.SET_NULL, related_name='headed_departments')

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
