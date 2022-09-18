from cgitb import text
from typing import Text
from django.db import models

from account.models import DoctorProfile, PatientProfile, PharmacistProfile,LabsProfile,X_rays_labProfile
from servicesmanager.models import Medicine,Tests ,X_Rays
# Create your models here.
class Visits(models.Model):
    """
    Visits model
    """

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"

    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name="patients",blank=True,null=True
    )
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name="doctors",blank=True,null=True
    )
    pharmacist = models.ForeignKey(
        PharmacistProfile, on_delete=models.CASCADE, related_name="pharmacist",blank=True,null=True
    )
    lab = models.ForeignKey(
        LabsProfile, on_delete=models.CASCADE, related_name="lab",blank=True,null=True
    )
    x_rays_lab = models.ForeignKey(
        X_rays_labProfile, on_delete=models.CASCADE, related_name="x_rays_lab",blank=True,null=True
    )
    summary = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    prescription = models.TextField(blank=True,null=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE,related_name="medicines",blank=True,null=True)
    test =  models.ForeignKey(Tests, on_delete=models.CASCADE,related_name="tests",blank=True,null=True)
    x_rays =  models.ForeignKey(X_Rays, on_delete=models.CASCADE,related_name="x_rayss",blank=True,null=True)
    visit_status = models.BooleanField(default=True)

    def __str__(self):
        return self.summary
