from pyexpat import model
from django.db import models

# Create your models here.

class employees(models.Model):
    emp_id = models.IntegerField()
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname


class projects(models.Model):
    pro_id = models.IntegerField()
    projectname = models.CharField(max_length=20)
    projectEmp = models.CharField(max_length=10)

    def __str__(self):
        return self.projectname
