from django.shortcuts import render
from .models import *

from django.http import JsonResponse
import json


# Create your views here.

def all_group(request):
    if request.user.is_authenticated:
        groups = Groub.objects.filter(activation=False).order_by('-id')
    else :
        groups = []
        print(groups)

    return render(request, 'index.html', {'groups':groups})

def all_group_true(request):
    if request.user.is_authenticated:
        groups = Groub.objects.filter(activation=True).order_by('-id')
    else :
        groups = []
        print(groups)

    return render(request, 'index.html', {'groups':groups})

def update_group(request):
    groupId = request.POST.get('groupId')
    action = request.POST.get("action")
    try:
        group, created = Groub.objects.get_or_create(id=groupId)
        if action == 'SE': # الموافقة على الطلب
            group.activation = True
            group.save()
        elif action == 'DE': # الحذف 
            group.delete()
        
    except:
        pass
    return JsonResponse('', safe=False)

def report(request):
    if request.user.is_authenticated:
        reports = Report.objects.order_by('-id')

    return render(request, 'report.html', {'reports':reports})
