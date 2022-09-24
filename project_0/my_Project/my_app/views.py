from django.shortcuts import render
from .models import Cuboid

# Create your views here.
def home(request):
    context = {'cuboids': Cuboid.objects.all()
    }
    return render (request,'my_app/home.html',context=context)