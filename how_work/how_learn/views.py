from django.shortcuts import render
from .models import ModelContent

def display(request):
    fm = ModelContent.objects.all
    return render(request, 'display.html', {'modell':fm})
