from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


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
    c = Animal.objects.filter(pk=post_id)
    context = {'post':c}
    return render(request,'info/post.html',context)

def addpost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'info/addpost.html', {'form': form})

def base(request):
    cat = Category.objects.all()
    return render(request,'info/base.html',{'cat':cat})