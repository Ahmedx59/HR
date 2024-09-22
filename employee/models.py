from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField(max_length=10)
    birth_day = models.DateField
    age = models.IntegerField(max_length=2)
    position_id = models.ForeignKey('Position',related_name=position_id , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Position(models.Model):
    name = models.CharField(max_length=50)
    years_of_experience = models.IntegerField(max_length=5)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    