from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from django.conf import settings

def dashboard_view(request):
    return render(request, "dashboard.html")

def aboutus_view(request):
    return render(request, "aboutus.html")

def contactus_view(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        if name and email and subject and message:
            recipient = 'admin0108@gmail.com'
            body = f'From: {name} <{email}>\n\nMessage:\n{message}'
            mail = EmailMessage(
                subject=f'[Contact Form] {subject}',
                body=body,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com'),
                to=[recipient],
                reply_to=[email] if email else None,
            )
            try:
                mail.send(fail_silently=False)
                context['success'] = True
            except BadHeaderError:
                context['error'] = 'Invalid header found.'
            except Exception as e:
                context['error'] = str(e)
        else:
            context['error'] = 'Please fill in all fields.'
    return render(request, 'contactus.html', context)

def faq_view(request):
    return render(request, "faq.html")

def debt_recovery_view(request):
    return render(request, "debt_recovery.html")

def our_system_view(request):
    return render(request, "our_system.html")

def service_offer_view(request):
    return render(request, "service_offer.html")

    