from django.shortcuts import render
from .models import Unit

# Create your views here.


def index(request):
    units = Unit.objects.all()
    return render(request, 'index.html', {'units': units})
