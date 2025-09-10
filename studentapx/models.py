from django.db import models

# Create your models here.
class studentRecord(models.Model):
    student_id=models.CharField(max_length=100)
    full_name=models.CharField(max_length=250)
    course=models.CharField(max_length=150)
    year_level=models.CharField(max_length=100)
    date_registered=models.DateTimeField(auto_now_add=True)