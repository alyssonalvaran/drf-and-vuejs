from django.urls import path
from jobs.api.views import (JobOfferListCreateAPIView, JobOfferDetailCreateAPIView)

urlpatterns = [
    path(
        "jobs/", 
        JobOfferListCreateAPIView.as_view(), 
        name="job-list"
    ),
    path(
        "jobs/<int:pk>/", 
        JobOfferDetailCreateAPIView.as_view(), 
        name="job-details"
    ),
]