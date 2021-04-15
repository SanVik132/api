from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator



user_type_data = ( ('1', "Teacher"), ('2', "Student"))
GENDER = (('male', 'Male'),('female', 'Female'),('other', 'Other'))
Blood_group = (('A+', 'A+'),('B+', 'B+'),('O+', 'O+'),('AB+', 'AB+'),('A-', 'A-'),('B-', 'B-'),('O-', 'O-'),('AB-', 'AB-'))
mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")


class User(AbstractUser):
    mobile = models.CharField(max_length=10,null = True)
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)



class OTPs(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    otp = models.CharField(max_length=15, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.user.first_name

class Student(models.Model):
    admission_number = models.CharField(max_length=200, unique=True,null = True)
    admin = models.OneToOneField(User, on_delete = models.CASCADE,null = True,blank = True)
    firstname = models.CharField(max_length=200,null = True)
    lastname = models.CharField(max_length=200,null = True)
    gender = models.CharField(max_length=10, choices=GENDER,null = True)
    blood_group = models.CharField(max_length=10, choices=Blood_group,null = True)
    date_of_birth = models.DateField(default=timezone.now,null = True)
    address = models.TextField(blank=True,null = True)
    parent_mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True,null = True)

    def __str__(self):
        return f'{self.lastname} {self.firstname} ({self.admission_number})'

class Teacher(models.Model):
    admin = models.OneToOneField(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=200,null = True)
    lastname = models.CharField(max_length=200,null = True)
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True,null = True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects = models.Manager()
    def __str__(self):
        return self.admin.username

@receiver(post_save, sender=User)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == '1':
            Teacher.objects.create(admin=instance)
        if instance.user_type == '2':
            Student.objects.create(admin=instance)
    
'''
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == '1':
        instance.teacher.save()
    if instance.user_type == '2':
        instance.student.save()
'''