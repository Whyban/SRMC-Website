from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("aboutus", views.aboutus_view, name="aboutus"),
    path("contactus", views.contactus_view, name="contactus"),
    path("careers", views.careers_view, name="careers"),
    path("our_partners", views.our_partners_view, name="our_partners"),
]