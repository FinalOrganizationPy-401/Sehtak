from django.urls import path
from .views import VisitsListCreateView, VisitsRetrieveUpdateDestroyView

urlpatterns = [
    path("", VisitsListCreateView.as_view(), name="visits_list"),
    path(
        "<int:pk>/",
        VisitsRetrieveUpdateDestroyView.as_view(),
        name="visits_detail",
    ),
    # view related visits_ for each 
]
