from django.urls import path
from .views import CreateVisitView, VisitsRetrieveUpdateDestroyView,UserVisitsView

urlpatterns = [
    path("", UserVisitsView.as_view(), name="visits_list"),

    path(
        "<int:pk>/",
        VisitsRetrieveUpdateDestroyView.as_view(),
        name="visits_detail",
    ),
    path("create/",CreateVisitView.as_view(), name="create_visit")
    # view related visits_ for each 
]
