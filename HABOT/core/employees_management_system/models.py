from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255) # Required 
    email = models.EmailField(unique=True)   # Required and unique 
    department = models.CharField(max_length=100, blank=True, null=True) # Optional 
    role = models.CharField(max_length=100, blank=True, null=True)       # Optional 
    date_joined = models.DateField(auto_now_add=True) # Auto set on creation                  

    def __str__(self):
        return self.name