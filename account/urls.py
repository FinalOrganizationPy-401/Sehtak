from django.urls import path
from account.views import MyObtainTokenPairView, RegisterView,PatientProfileView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    # path('profile/', PatientProfileView.as_view(), name='patient_profile'),
    path('profile/<int:pk>', PatientProfileView.as_view(), name='patient_profile'),

]