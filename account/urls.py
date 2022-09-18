from django.urls import path
from account.views import MyObtainTokenPairView, RegisterView,PatientProfileView,DoctorProfileView,DoctorView ,PharmacistView,PharmacistProfileView, LabsView, LabProfileView,X_raysView,X_raysProfileView,DoctorProfileEdit,PharmacistProfileEdit,PharmacistProfileEdit,LabsProfileEdit,X_raysProfileEdit
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),

    path('profile/<int:pk>/', PatientProfileView.as_view(), name='patient_profile'),

    path('doctors/', DoctorView.as_view(), name='doctor_list'),
    path('doctors/profile/<int:pk>', DoctorProfileView.as_view(), name='doctor_profile'),
    path('doctors/profile/edit/<int:pk>', DoctorProfileEdit.as_view(), name='doctor_edit'),

    path('pharmacists/', PharmacistView.as_view(), name='pharmacist_list'),
    path('pharmacist/profile/<int:pk>', PharmacistProfileView.as_view(), name='pharmacist_profile'),
    path('pharmacist/profile/edit/<int:pk>', PharmacistProfileEdit.as_view(), name='doctor_edit'),

    path('labs/', LabsView.as_view(), name='lab_list'),
    path('labs/profile/<int:pk>', LabProfileView.as_view(), name='lab_profile'),
    path('labs/profile/edit/<int:pk>', LabsProfileEdit.as_view(), name='doctor_edit'),

    path('x_rays/', X_raysView.as_view(), name='x_ray_list'),
    path('x_rays/profile/<int:pk>', X_raysProfileView.as_view(), name='x_ray_profile'),
    path('x_rays/profile/edit/<int:pk>', X_raysProfileEdit.as_view(), name='doctor_edit'),

]