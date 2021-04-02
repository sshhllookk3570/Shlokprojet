from django.db import models

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
   # address=models.CharField(max_length=20)
    age=models.IntegerField()
    T_mark=models.IntegerField()


# model for Address of student

class Address(models.Model):
     stud=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='addr_set')
     address=models.CharField(max_length=20)

