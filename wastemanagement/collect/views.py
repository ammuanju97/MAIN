
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from collect.models import AddProduct, CollectDetails
from django.http import HttpResponse
from django.contrib import messages
from common.models import AddRecycle
from user.models import CollectRegister1, Sell
# Create your views here.


def addproducts(request):
    s=AddRecycle.objects.all()
    return render(request, 'addproducts.html',{'s':s})

def addsell(request):
    if request.method == 'POST':
        user = request.POST['name']
        productname = request.POST['productname']
        weight = request.POST['weight']
        price = request.POST['price']
        date = request.POST['date']
        add=AddProduct(user=user, productname=productname, weight=weight, price=price, date=date, status="notbooked")
        add.save()
    return redirect('addproducts')

def userbuy(request):
    det=AddProduct.objects.filter()
    return render(request, 'userbuy.html', {'det':det})

def buyfun(request,id):
    bu=AddProduct.objects.get(id=id)
    bu.status="booked"
    bu.save()
    return render(request, 'byustatus.html' , {'bu':bu})

def byustatus(request):
    return render(request, 'byustatus.html')

def ordertable(request):
    return render(request,'ordertable.html')

def orderfun(request,id):
    if request.method=='POST':
       sta=request.POST['status']
       u=request.POST['email']
       v=request.POST['name']
       bu=AddProduct.objects.get(id=id)
       bu.status=sta
       bu.save()
       bu.user=u
       bu.save()
       bu.usname=v
       bu.save()
       return redirect('buyfun',id)
    else:
        return render(request,'byustatus.html')   

   
def editprofile(request,cname):
    u=CollectRegister1.objects.filter(username=cname)
    return render(request, 'editprofile.html', {'u':u})

def collectprofile(request,cname):
    if request.method == 'POST':
        cstate = request.POST['state']
        cdistrict = request.POST['district']
        ccity = request.POST['city']
        cpin = request.POST['pin']
        cmobileno = request.POST['mobileno']
        u = CollectRegister1.objects.get(username=cname)
        u.state = cstate
        u.save()
        u.district = cdistrict
        u.save()
        u.city = ccity
        u.save()
        u.pin = cpin
        u.save()
        u.mobileno = cmobileno
        u.save()
        return redirect('editprofile',cname)
    else:
        return redirect('editprofile',cname)

def payment(request):
    return render(request, 'payment.html')

def notifications(request):
    noti=Sell.objects.filter()
    return render(request, 'notifications.html', {'noti':noti})

def colfun(request,id,cname):
    cb=Sell.objects.get(id=id)
    cb.status="booked"
    cb.save()
    cb.cname=cname
    cb.save()
    return render(request, 'collect.html',{'cb':cb})

def colorder(request,id):
    if request.method == 'POST':
       sta=request.POST['status']
       u=request.POST['email']
       v=request.POST['name']
       cb=Sell.objects.get(id=id)
       cb.status=sta
       cb.save()
       cb.user=u
       cb.save()
       cb.usname=v
       cb.save()
       return redirect('colfun',id)
    else:
        return render(request,'collect.html')


def collectingagent(request,name):
    c1 = Sell.objects.filter(status="booked")
    return render(request, 'collectingagent.html',{'c1':c1})

def sitevisit(request,name,id):
    sv=Sell.objects.get(user=name,id=id)
    return render(request, 'sitevisit.html',{'sv':sv})

def collectvisit(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        cname = request.POST['cname']
        wastetype = request.POST['wastetype']
        weight = request.POST['weight']
        price = request.POST['price']
        date = request.POST['date22']
        coll=CollectDetails(username=username, email=email, cname=cname, wastetype=wastetype, weight=weight, price=price, date=date)
        coll.save()
        return render(request, 'sitevisit.html')
        
def visitdate(request,username):
    vd=CollectDetails.objects.filter(email=username)
    return render(request,'visitdate.html',{'vd':vd})