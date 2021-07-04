from django.shortcuts import render

from .models import basicpack
from .models import standardpack
from .models import propack
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def orders(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        send_mail(name,
                  message,
                  settings.EMAIL_HOST_USER,
                  ['nspxbdd@gmail.com'],
                  fail_silently=False
                  )

        orderdata = basicpack(name=name, email=email,
                              number=number, message=message)
        orderdata.save()

        return render(request, "thankyou.html", {'number': number, 'message': message, 'sender_name': name})


def orders2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        send_mail(name,
                  message,
                  settings.EMAIL_HOST_USER,
                  ['nspxbdd@gmail.com'],
                  fail_silently=False
                  )

        orderdata2 = standardpack(name=name, email=email,
                              number=number, message=message)
        orderdata2.save()

        return render(request, "thankyou.html", {'number': number, 'message': message, 'sender_name': name})


def orders3(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        send_mail(name,
                  message,
                  settings.EMAIL_HOST_USER,
                  ['nspxbdd@gmail.com'],
                  fail_silently=False
                  )

        orderdata3 = propack(name=name, email=email,
                              number=number, message=message)
        orderdata3.save()

        return render(request, "thankyou.html", {'number': number, 'message': message, 'sender_name': name})