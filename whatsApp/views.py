from django.shortcuts import render
from .models import *

# Create your views here.

def all_group(request):
    if request.user.is_authenticated:
        groups = Groub.objects.order_by('-id')

    return render(request, 'index.html', {'groups':groups})

def update_group(request):
    groupId = request.POST.get('groupId')
    action = request.POST.get("action")
    try:
        group, created = Groub.objects.get_or_create(id=groupId, activation=False)
        if group == 'SE': # الموافقة على الطلب
            group.activation = True
            group.save()
        elif group == 'DE': # تم التوصيل
            group.delete()
        
    except:
        pass
    return JsonResponse(f'تمت الموافقة على الطلب رقم ..  {groupId}', safe=False)
