# from weakref import proxy
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField
# from account.models import Patient


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"
        PHARMACIST = "PHARMACIST", "Pharmacist"
        LABS = "LABS", "Labs"
        X_RAYS_LAB = "X_RAYS_LAB", "X_rays_lab"

    base_role = Role.ADMIN

    username = "Abo azim"
    email = models.EmailField( unique=True) # changes email to unique and blank to false
    role = models.CharField(max_length=50, choices=Role.choices)
    # if role == 'PATIENT':
    # user_info = models.OneToOneField(PatientProfile, on_delete=models.CASCADE,null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # self.role = self.base_role
            self.role = self.role or self.base_role
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
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created and instance.role == "PATIENT":
        PatientProfile.objects.create(user=instance)



class PatientProfile(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    BLOOD_CHOICES = [
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_user_id')
    first_name = models.CharField(max_length=256, blank=True,null=True)
    last_name = models.CharField(max_length=256, blank=True,null=True)
    # phone = phone = PhoneNumberField(blank=True,null=True)
    phone =PhoneNumberField(blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)

    gender = models.IntegerField(choices=GENDER_CHOICES,blank=True,null=True)
    height = models.PositiveIntegerField(blank=True,null=True)
    weight = models.PositiveIntegerField(blank=True,null=True)
    blood_type = models.CharField( max_length=50, choices=BLOOD_CHOICES,default='AB+',blank=True,null=True)
    allergies = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.email
        # return self.first_name


# ProfessionalProfile

class ProfessionalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True,null=True)
    phone = PhoneNumberField(blank=True)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7,default='31.959153316146658,35.91156005859375')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

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



class DoctorProfile(ProfessionalProfile):
    pass


@receiver(post_save, sender=Doctor)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "DOCTOR":
        DoctorProfile.objects.create(user=instance)


# Pharmacist Profile
class PharmacistManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PHARMACIST)


class Pharmacist(User):

    base_role = User.Role.PHARMACIST
    Pharmacist = PharmacistManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Pharmacist)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created and instance.role == "PHARMACIST":
        PharmacistProfile.objects.create(user=instance)


class PharmacistProfile(ProfessionalProfile):
    pass


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


class LabsProfile(ProfessionalProfile):
    pass


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


class X_rays_labProfile(ProfessionalProfile):
    pass


@receiver(post_save, sender=X_rays_lab)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "X_RAYS_LAB":
        X_rays_labProfile.objects.create(user=instance)
