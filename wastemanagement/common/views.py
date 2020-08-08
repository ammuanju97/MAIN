from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from common.models import AddCategory, AddRecycle
from django.http import HttpResponse
from django.contrib import messages
from user.models import UserRegister, CollectRegister1
from collect.models import Payment, SellPayment
# Create your views here.
def category(request):
    return render(request, 'category.html')

def adminhome(request):
    return render(request, 'adminhome.html')

def addcategory(request):
    if request.method == 'POST':
        categoryname = request.POST['categoryname']
        
        addcat = AddCategory(categoryname=categoryname)
        addcat.save()
        return render(request, 'category.html')

def category1(request):
    return render(request, 'category1.html')

def addrecycle(request):
    if request.method == 'POST':
        categoryname = request.POST['categoryname']
        addre = AddRecycle(categoryname=categoryname)
        addre.save()
        return render(request, 'category1.html')


def adminhome1(request):
    a1=Payment.objects.filter()
    return render(request, 'adminhome1.html', {'a1':a1})

def adminhome2(request):
    a2=SellPayment.objects.filter()
    return render(request, 'adminhome2.html', {'a2':a2})

def addadmin(request):
    return render(request, 'addadmin.html')


def viewuserlist(request):
    u1=UserRegister.objects.filter()
    return render(request, 'viewuserlist.html', {'u1':u1})

def viewcollect(request):
    v1=CollectRegister1.objects.filter()
    return render(request, 'viewcollect.html',{'v1':v1})

def approvcollect(request):
    v2=CollectRegister1.objects.filter()
    return render(request, 'approvcollect.html',{'v2':v2})



