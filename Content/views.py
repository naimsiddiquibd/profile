from django.shortcuts import render
from Content.models import Settings
from Content.models import Logo
from Content.models import Menu
from banner.models import banner
from banner.models import sm
from banner.models import hireme
from about.models import about
from about.models import skills
from about.models import counter
from services.models import services
from services.models import items
from experience.models import experience
from experience.models import education
from experience.models import workhis
from portfolio.models import porthead
from portfolio.models import itemsb
from pricing.models import pricehead
from pricing.models import pricetable
from contact.models import conthead
import re, random
# Create your views here.


def Home(request):
    settings = Settings.objects.all()
    logodata = Logo.objects.all()
    menudata = Menu.objects.all()
    bannerdata = banner.objects.all()
    smdata = sm.objects.all()
    hiremedata = hireme.objects.all()
    aboutdata = about.objects.all()
    skilldata = skills.objects.all()
    counterdata = counter.objects.all()
    servicesdata = services.objects.all()
    itemsdata = items.objects.all()
    experiencedata = experience.objects.all()
    educationdata = education.objects.all()
    workdata = workhis.objects.all()
    portdata = porthead.objects.all()
    itemsbdata = itemsb.objects.all()
    pricedata = pricehead.objects.all()
    pricetabledata = pricetable.objects.all()
    contheaddata = conthead.objects.all()

    context = {
        'settings': settings,
        'logo': logodata,
        'menu': menudata,
        'ban': bannerdata,
        'sm': smdata,
        'hire': hiremedata,
        'about': aboutdata,
        'skill': skilldata,
        'counter': counterdata,
        'services': servicesdata,
        'item': itemsdata,
        'exp': experiencedata,
        'edu': educationdata,
        'work': workdata,
        'port': portdata,
        'itemb': itemsbdata,
        'price': pricedata,
        'table': pricetabledata,
        'cont': contheaddata,
    }
    return render(request, 'home.html', context)
