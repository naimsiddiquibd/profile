from django.shortcuts import render
from .models import txtmessages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def emails(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(subject,
                  message,
                  settings.EMAIL_HOST_USER,
                  ['nspxbdd@gmail.com'],
                  fail_silently=False
                  )

        emaildata = txtmessages(name=name, email=email,
                                subject=subject, message=message)
        emaildata.save()

        return render(request, "thankyou.html", {'subject': subject, 'message': message, 'sender_name': name})
