from django.shortcuts import render

# Create your views here.

def all_group(request):
    if request.user.is_authenticated:
        groups = Groub.objects.all()

    return render(request, 'product_detail.html', {'groups':groups})

