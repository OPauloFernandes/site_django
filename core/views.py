from django.shortcuts import render
from django.http import HttpResponse
from .models import Home, About

# Create your views here.
def home(request):

    home = Home.objects.all().first()
    about = About.objects.all().first()


    context= {
        'name': home.name,
        'role1': home.role1,
        'role2': home.role2,
        'bd': about.bd
    }

    return render(request, 'index.html', context)