from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    birth_day = models.DateField
    age = models.IntegerField()
    position_id = models.ForeignKey('Position',related_name='position_id' , on_delete=models.CASCADE ,blank=True, null=True)

    def __str__(self):
        return self.name
    

class Position(models.Model):
    name = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    