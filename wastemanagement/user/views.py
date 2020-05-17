from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from user.models import UserRegister, CollectRegister1, Sell
from django.http import HttpResponse
from django.contrib import messages
from collect.models import AddProduct
from common.models import AddCategory
# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html') 

def collect(request):
    return render(request, 'collect.html')

def collectingagenthome(request):
    return render(request, 'collectingagenthome.html')

def collectservice(request):
    return render(request, 'collectservice.html')

def login(request):
    return render(request, 'login.html')

def ordertable(request):
    return render(request, 'ordertable.html')

def  productdetails(request):
    return render(request, 'productdetails.html')

def recycleservice(request):
    return render(request, 'recycleservice.html')

def recyclingagenthome(request):
    return render(request, 'recyclingagenthome.html')

def removeproducts(request):
    return render(request, 'removeproducts.html')

def sell(request):
    s=AddCategory.objects.all()
    return render(request, 'sell.html',{'s':s})

def sellservice(request):
    return render(request, 'sellservice.html')

def signup(request):
    return render(request, 'signup.html')

def userhome(request):
    return render(request, 'userhome.html')

def viewproducts(request):
    list1 = ViewProduct.objects.all()
    return render(request, 'viewproducts.html', {'list1':list1})

def wastedetails(request):
    return render(request, 'wastedetails.html')

def signup1(request):
    return render(request, 'signup1.html')



def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        housenumber = request.POST['housenumber']
        state = request.POST['state']
        district = request.POST['district']
        city = request.POST['city']
        pin = request.POST['pin']
        mobileno = request.POST['mobileno']
        usertype = request.POST['usertype']
        email = request.POST['email']
        password = request.POST['password']
        uname = fname+ "" +lname

        if User.objects.filter(username=email).exists():
            print('user taken')
            return redirect('login')
        else:
            user = User.objects.create_user(username=email, password=password, email=email, first_name=fname, last_name=lname)
            user.save()
            u = UserRegister(username=email, name=uname, housenumber=housenumber, state=state, district=district, city=city, pin=pin, mobile=mobileno, usertype=usertype)  
            u.save()
            print('user created')
            return redirect('login')
    else:
        return render(request, 'signup.html')


def signup1(request):
    if request.method == 'POST':
        
        cname = request.POST['cname']
        state = request.POST['state']
        district = request.POST['district']
        city = request.POST['city']
        pin = request.POST['pin']
        mobileno = request.POST['mobileno']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            print('username taken')
            return redirect('login')
        else:
            user = User.objects.create_user(username=email, password=password, email=email, first_name=cname, last_name="Agent")
            user.save()
            u1 = CollectRegister1(username=email, cname=cname, state=state, district=district, city=city, pin=pin, mobile=mobileno)
            u1.save()
            print('collecting system created')
            return redirect('login')
    else:
        return render(request, 'signup1.html')

        
def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        if username=='admin' and  password=='admin':
            return redirect('adminhome')
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if User.objects.filter(username=username, last_name="Agent").exists():
                    return  redirect('collectingagenthome')
                else:
                    return redirect('userhome')
            else:
                messages.info(request, 'invalid credintail')
            return render(request,'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def userprofile(request,uname):
    m = UserRegister.objects.filter(username=uname)
    return render(request, 'userprofile.html',{'m':m})

def saveprofile(request,uname):
    if request.method == 'POST':
       
        nhousenumber = request.POST['housenumber']
        nstate = request.POST['state']
        ndistrict = request.POST['district']
        ncity = request.POST['city']
        npin = request.POST['pin']
        nmobileno = request.POST['mobileno'] 
        
        m = UserRegister.objects.get(username=uname) 
        
        m.housenumber = nhousenumber
        m.save()
        m.state = nstate
        m.save()
        m.district = ndistrict
        m.save()
        m.city = ncity
        m.save()
        m.pin = npin
        m.save()
        m.mobile = nmobileno
        m.save()
       
        return redirect('userprofile',uname)

    else:
        return redirect('userprofile',uname)    

def viewcollectingsystem(request):
    m1 = CollectRegister1.objects.filter()
    return render(request, 'viewcollectingsystem.html',{'m1':m1})


def selltype(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        cname = request.POST['cname']
        wastetype =request.POST['wastetype']
        weight = request.POST['weight']
       
        price = request.POST['price']
        s=Sell(user=name, email=email, cname=cname, wastetype=wastetype, weight=weight, price=price, status="notbooked")
        s.save()
        return redirect('sell')













def usertype(request):
    
    return render(request,'usertype.html')
   




