from django.shortcuts import render

def dashboard_view(request):
    return render(request, "dashboard.html")

def aboutus_view(request):
    return render(request, "aboutus.html")

def contactus_view(request):
    return render(request, "contactus.html")

def faq_view(request):
    return render(request, "faq.html")

def debt_recovery_view(request):
    return render(request, "debt_recovery.html")

def our_system_view(request):
    return render(request, "our_system.html")

def service_offer_view(request):
    return render(request, "service_offer.html")

    