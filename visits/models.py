from cgitb import text
from typing import Text
from django.db import models

from accounts.models import Patient,Doctor,Pharmacist,Labs,X_rays_lab

# Create your models here.
class Visits(models.Model):
    """
    Visits model 
    """
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="patient")
    doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="doctor")
    pharmacist_id =models.ForeignKey(Pharmacist,on_delete=models.CASCADE,related_name="pharmacist")
    lab_id =models.ForeignKey(Labs,on_delete=models.CASCADE,related_name="lab")
    x_rays_lab_id =models.ForeignKey(X_rays_lab,on_delete=models.CASCADE,related_name="x_rays_lab")
    summary = models.TextField()
    description =models.TextField()
    prescription = models.TextField()
    medicine_id = models.IntegerField()
    test_id = models.IntegerField()
    x_rays_id = models.IntegerField()
