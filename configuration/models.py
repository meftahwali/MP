from django.db import models

# Create your models here.

class Adminstration(models.Model):
    Libelle_admi_ar = models.CharField(max_length=200, blank=True, null=True)
    Libelle_admi_fr = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Libelle_fr
    def __unicode__(self):
        return self.Libelle_ar

class SousAdminstration(models.Model):
    Libelle_sousadmi_ar = models.CharField(max_length=200, blank=True, null=True)
    Libelle_sousadmi_fr = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Libelle_sousadmi_fr

    def __unicode__(self):
        return self.Libelle_sousadmi_ar
    
class Grade(models.Model):
    Libelle_grade_ar = models.CharField(max_length=200, blank=True, null=True)
    Libelle_grade_fr = models.CharField(max_length=200, blank=True, null=True) 
    def __str__(self):
        return self.Libelle_grade_fr

    def __unicode__(self):
        return self.Libelle_grade_ar
    
    


