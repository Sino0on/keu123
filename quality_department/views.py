from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html', {'educations': Education.objects.all()})


def disciplines(request, pk):
    return render(request, 'discipline.html', {'disciplines': Discripline.objects.filter(education=pk)})

