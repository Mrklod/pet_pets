from django.shortcuts import render,get_object_or_404
from .models import *

def index(request):
    cat = Category.objects.all()
    ani = Animal.objects.all()
    context = {'cat':cat,'animal':ani}
    return render(request,'info/index.html',context=context)

def contact(request):
    return render(request,'info/contact.html')

def us(request):
    return render(request,'info/us.html')

def read(request,post_id):
    post = get_object_or_404(Animal,pk=post_id)
    return render(request,'info/post.html',{'post':post})