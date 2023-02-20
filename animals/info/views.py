from django.shortcuts import render
from .models import *

def index(request):
    cat = Category.objects.all()
    ani = Animal.objects.all()
    context = {'cat':cat,'animal':ani}
    return render(request,'info/index.html',context=context)
