from cgitb import text
from typing import Text
from django.db import models

from account.models import DoctorProfile, PatientProfile

# Create your models here.
class Visits(models.Model):
    """
    Visits model
    """

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"

    # patient_id = models.ForeignKey(
    #     PatientProfile, on_delete=models.CASCADE, related_name="patients"
    # )
    # doctor_id = models.ForeignKey(
    #     DoctorProfile, on_delete=models.CASCADE, related_name="doctors"
    # )
    # pharmacist_id = models.ForeignKey(
    #     Pharmacist, on_delete=models.CASCADE, related_name="pharmacist"
    # )
    # lab_id = models.ForeignKey(Labs, on_delete=models.CASCADE, related_name="lab")
    # x_rays_lab_id = models.ForeignKey(
    #     X_rays_lab, on_delete=models.CASCADE, related_name="x_rays_lab"
    # )
    summary = models.TextField()
    description = models.TextField()
    prescription = models.TextField()
    medicine_id = models.IntegerField()
    test_id = models.IntegerField()
    x_rays_id = models.IntegerField()

    def __str__(self):
        return self.summary
