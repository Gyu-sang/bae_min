from django.shortcuts import render
from .models import Shop

# Create your views here.

def index(request):
    return render(request, 'baemin/index.html', {
        'shop_list': Shop.objects.all(),
    })
