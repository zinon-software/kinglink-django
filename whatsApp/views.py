from django.shortcuts import render
from .models import *

# Create your views here.

def all_group(request):
    if request.user.is_authenticated:
        groups = Groub.objects.all()

    return render(request, 'index.html', {'groups':groups})

