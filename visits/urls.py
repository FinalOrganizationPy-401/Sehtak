from django.urls import path
from .views import VisitsListCreateView, VisitsRetrieveUpdateDestroyView

urlpatterns= [
path('visits/', VisitsListCreateView.as_view(), name= "visits_list"),
path('visits/<int:pk>/', VisitsRetrieveUpdateDestroyView.as_view(), name= "visits_detail")
]

