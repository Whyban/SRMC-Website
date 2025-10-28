from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("aboutus", views.aboutus_view, name="aboutus"),
    path("contactus", views.contactus_view, name="contactus"),
    path("faq", views.faq_view, name="faq"),
    path("debt_recovery", views.debt_recovery_view, name="debt_recovery"),
    path("our_system", views.our_system_view, name="our_system"),
    path("service_offer", views.service_offer_view, name="service_offer"),
]