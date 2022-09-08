from django.urls import path

from .views import MedicineListCreateView , MedicineRetrieveUpdateDestroyView, TestsListCreateView , TestsRetrieveUpdateDestroyView , X_RaysListCreateView , X_RaysRetrieveUpdateDestroyView

urlpatterns = [
    path('medicen/', MedicineListCreateView.as_view(),name='medicens_list' ),
    path('medicen/<int:pk>/', MedicineRetrieveUpdateDestroyView.as_view(),name='medicen_detail'),

    path('test/', TestsListCreateView.as_view(),name='test_list' ),
    path('test/<int:pk>/', TestsRetrieveUpdateDestroyView.as_view(),name='test_detail'),

    path('x_ray/', X_RaysListCreateView.as_view(),name='x_ray_list' ),
    path('x_ray/<int:pk>/', X_RaysRetrieveUpdateDestroyView.as_view(),name='x_ray_detail')


]