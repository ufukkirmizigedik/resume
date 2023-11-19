from django.shortcuts import render
from core.models import *

# Create your views here.
def index(request):
    site_title_obj = GeneralSettings.objects.get(name = 'site_title')
    meslek_adi_obj = GeneralSettings.objects.get(name = 'meslek_adi')
    selamlama_obj = GeneralSettings.objects.get(name = 'hello')
    context = {
        'site_title' : site_title_obj.parameters,
        'meslek_adi' : meslek_adi_obj.parameters,
        'hello' : selamlama_obj.parameters,
    }

    return render(request,'index.html',context=context)

def contact(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog.html')
