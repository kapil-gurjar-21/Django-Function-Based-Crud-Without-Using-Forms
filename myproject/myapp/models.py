from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True,null=False,blank=True)
    teacher_name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    school=models.CharField(max_length=50)

