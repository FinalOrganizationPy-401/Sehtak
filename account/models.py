from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"
        # PHARMACIST = "PHARMACIST", "Pharmacist"
        # LABS = "LABS", "Labs"
        # X_RAYS_LAB = "X_RAYS_LAB", "X_rays_lab"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PATIENT)


class Patient(User):

    base_role = User.Role.PATIENT

    student = PatientManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Patient"


@receiver(post_save, sender=Patient)
def create_user_profile(sender, instance, created,*args, **kwargs):
    if created and instance.role == "PATIENT":
        PatientProfile.objects.create(user=instance)


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_id = models.IntegerField(null=True, blank=True)



# DOCTOR = "DOCTOR", "Doctor"

class DoctorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.DOCTOR)


class Doctor(User):

    base_role = User.Role.DOCTOR

    doctor = DoctorManager()

    class Meta:
        proxy = True



class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Doctor)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "DOCTOR":
       DoctorProfile.objects.create(user=instance)