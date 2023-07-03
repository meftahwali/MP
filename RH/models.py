from django.db import models

# Create your models here
class Employee(models.Model):
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )

    
    name_ar = models.CharField(max_length=100, verbose_name="Name(AR)", blank=True, null=True)
    prenom_ar = models.CharField(max_length=100, blank=True, null=True)
    name_fr = models.CharField(max_length=100, blank=True, null=True)
    prenom_fr = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)
    photo_emp = models.CharField(max_length=100, blank=True, null=True)
    date_naissance = models.CharField(max_length=100, blank=True, null=True)
    lieu_naissance = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.name_ar

