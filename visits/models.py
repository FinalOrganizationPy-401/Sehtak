from django.db import models
# from django.utils import timezone
from account.models import DoctorProfile, PatientProfile, PharmacistProfile,LabsProfile,X_rays_labProfile
# from servicesmanager.models import Medicine,Tests ,X_Rays
# Create your models here.
class Visits(models.Model):
    """
    Visits model
    """
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name="patients",blank=True,null=True
    )
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name="doctors",blank=True,null=True
    )
    description = models.TextField(blank=True,null=True)
    medicine = models.TextField(blank=True,null=True)
    medicine_status = models.BooleanField(default=False)
    
    test_description =models.TextField(blank=True,null=True)
    test_attachments = models.TextField(blank=True,null=True)

    x_rays_description =models.TextField(blank=True,null=True)
    x_rays_attachments = models.TextField(blank=True,null=True)
    visit_status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"
        
    def __str__(self):
        return self.description

    # medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE,related_name="medicines",blank=True,null=True)

        # prescription = models.TextField(blank=True,null=True)

     # pharmacist = models.ForeignKey(
    #     PharmacistProfile, on_delete=models.CASCADE, related_name="pharmacist",blank=True,null=True
    # )
    # lab = models.ForeignKey(
    #     LabsProfile, on_delete=models.CASCADE, related_name="lab",blank=True,null=True
    # )
    # x_rays_lab = models.ForeignKey(
    #     X_rays_labProfile, on_delete=models.CASCADE, related_name="x_rays_lab",blank=True,null=True
    # )
    # test_attachments =  models.ForeignKey(Tests, on_delete=models.CASCADE,related_name="tests",blank=True,null=True)
    # x_rays =  models.ForeignKey(X_Rays, on_delete=models.CASCADE,related_name="x_rayss",blank=True,null=True)
 
    # current_time = timezone.now().strftime('%H:%M:%S')
    # last_update = models.DateField(auto_now=True)
    
    