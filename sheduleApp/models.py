from django.db import models

# Create your models here.
class Student(models.Model):
    stu_nic = models.CharField(primary_key=True, max_length=15)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    job_role = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    stu_password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'



class Interview(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    stu_nic = models.ForeignKey('Student', models.DO_NOTHING, db_column='stu_nic', blank=True, null=True)
    position = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interview'
