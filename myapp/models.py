from django.db import models


class Teacher(models.Model):
	class Meta:
		abstract=True
	teacher_name=models.CharField(max_length=10)	
	teacher_email=models.EmailField()

class Student(Teacher):


   name = models.CharField(max_length = 20)
   gender= models.CharField(max_length =10)
   mail= models.CharField(max_length = 50)
   password1=models.CharField(max_length=8)
   phone = models.IntegerField()
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True, null=True, blank=True)
   class Meta:
   	 db_table='student'

