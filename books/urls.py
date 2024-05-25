from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('', BookView.as_view(), name='list'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('<int:pk>/reviews/', AddReviewVIEW.as_view(), name='reviews'),
    path('<int:book_id>/<int:review_id>/edit/', EditReviewVIEW.as_view(), name='edit_review'),
    path('<int:book_id>/<int:review_id>/delete/confirm/', ConfirmDeleteReviewVIEW.as_view(), name='confirm_delete_review'),
    path('<int:book_id>/<int:review_id>/delete/', DeleteReviewVIEW.as_view(), name='delete_review')
]