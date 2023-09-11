from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index),
    path("", views.ReviewView.as_view()),
    path("thanks", views.thank_you),
]
