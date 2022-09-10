from weakref import proxy
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"
        PHARMACIST = "PHARMACIST", "Pharmacist"
        LABS = "LABS", "Labs"
        X_RAYS_LAB = "X_RAYS_LAB", "X_rays_lab"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

# Patient Profile

class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PATIENT)


class Patient(User):

    base_role = User.Role.PATIENT

    patient = PatientManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Patient)
def create_user_profile(sender, instance, created,*args, **kwargs):
    if created and instance.role == "PATIENT":
        PatientProfile.objects.create(user=instance)


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_id = models.IntegerField(null=True, blank=True)



# DOCTOR Profile

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


# Pharmacist Profile
class PharmacistManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PHARMACIST)

class Pharmacist(User):

    base_role = User.Role.PHARMACIST
    Pharmacist = PharmacistManager()

    class Meta:
        proxy = True

@receiver(post_save,sender=Pharmacist)
def create_user_profile(sender, instance, created,*args, **kwargs):
    if created and instance.role == "PHARMACIST":
        PharmacistProfile.objects.create(user=instance)

class PharmacistProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pharmacist_id = models.IntegerField(null=True,blank=True)


# Labs Profile

class LabsManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.LABS)


class Labs(User):

    base_role = User.Role.LABS

    Labs = LabsManager()

    class Meta:
        proxy = True



class LabsProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    labs_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Labs)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "LABS":
       LabsProfile.objects.create(user=instance)



# X_rays_lab Profile

class X_rays_labManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.X_RAYS_LAB)


class X_rays_lab(User):

    base_role = User.Role.X_RAYS_LAB

    x_rays_lab = X_rays_labManager()

    class Meta:
        proxy = True



class X_rays_labProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    x_rays_lab_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=X_rays_lab)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "X_RAYS_LAB":
       X_rays_labProfile.objects.create(user=instance)
