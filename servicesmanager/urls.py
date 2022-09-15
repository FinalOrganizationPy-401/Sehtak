from django.urls import path

from .views import (
    MedicineListCreateView,
    MedicineRetrieveUpdateDestroyView,
    TestsListCreateView,
    TestsRetrieveUpdateDestroyView,
    X_RaysListCreateView,
    X_RaysRetrieveUpdateDestroyView,
)

# from ..visits.views import VisitsListCreateView, VisitsRetrieveUpdateDestroyView

urlpatterns = [
    path("medicine/", MedicineListCreateView.as_view(), name="medicines_list"),
    path(
        "medicine/<int:pk>/",
        MedicineRetrieveUpdateDestroyView.as_view(),
        name="medicine_detail",
    ),
    path("test/", TestsListCreateView.as_view(), name="test_list"),
    path(
        "test/<int:pk>/", TestsRetrieveUpdateDestroyView.as_view(), name="test_detail"
    ),
    path("x_ray/", X_RaysListCreateView.as_view(), name="x_ray_list"),
    path(
        "x_ray/<int:pk>/",
        X_RaysRetrieveUpdateDestroyView.as_view(),
        name="x_ray_detail",
    ),

    # path("visits/", VisitsListCreateView.as_view(), name="visits_list"),
    # path(
    #     "visits/<int:pk>/",
    #     VisitsRetrieveUpdateDestroyView.as_view(),
    #     name="visits_detail",
    # ),
]
