from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index),#-------------------------------------------def
    # path("", views.ReviewView.as_view()),#----------------------------[Classic View]-ok
    # path("", views.ReviewView3.as_view()),#---------------------------[FormView] -ok
    path("", views.ReviewView4.as_view()), #----------------------------[CreateView]--super
    path("thanks", views.thank_you),#-----------------------------------[def]--super
    path("thank-you", views.ThankYouView.as_view()), #------------------TemplateView
    # path("reviews", views.ReviewListView.as_view()),#-----------------TemplateView
    path("reviews2", views.ReviewListView2.as_view()),#-----------------[ListView]--super
    # path("reviews/<int:rev_id>", views.SingleReviewView.as_view()),#--TemplateView
    path("reviews/<int:pk>", views.SingleReviewView2.as_view()),#-------[DetailView]--super

]
