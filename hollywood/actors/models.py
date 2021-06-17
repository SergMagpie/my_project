from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField()
    height = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
# CRUD
# C - create
# R - read
# U - update
# D - delete
# lt,gt, lte, gte - less than, greater than, 
# 185 195 включительно