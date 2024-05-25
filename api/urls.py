from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path("reviews/", BookReviewListAPIView.as_view(), name="review-list"),
    path("reviews/<int:id>/", BookReviewDetailAPIView.as_view(), name="review-detail"),
]
