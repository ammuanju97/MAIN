from django . urls import path
from . import views


urlpatterns = [
path('',views.home, name='home'),
path('aboutus/',views.aboutus, name='aboutus'),
# path('adminhome/',views.adminhome, name='adminhome'),
path('collect/',views.collect,name='collect'),
path('collectingagenthome/',views.collectingagenthome,name='collectingagenthome'),
path('collectservice/',views.collectservice,name='collectservice'),
path('login/',views.login,name='login'),
path('ordertable/',views.ordertable,name='ordertable'),
path('productdetails/',views.productdetails,name='productdetails'),
path('recycleservice/',views.recycleservice,name='recycleservice'),
path('recyclyingagenthome/',views.recyclingagenthome,name='recyclingagenethome'),
path('removeproducts/',views.removeproducts,name='removeproducts'),
path('sell/',views.sell,name='sell'),
path('selltype/',views.selltype,name='selltype'),
path('sellservice/',views.sellservice,name='sellservice'),
path('signup/',views.signup,name='signup'),
path('signup1/',views.signup1,name='signup1'),
path('userhome/',views.userhome,name='userhome'),
path('userprofile/<str:uname>',views.userprofile,name='userprofile'),
path('saveprofile/<str:uname>',views.saveprofile,name='saveprofile'),
path('viewproducts/',views.viewproducts,name='viewproducts'),
path('viewcollectingsystem/',views.viewcollectingsystem,name='viewcollectingsystem'),


path('wastedetails/',views.wastedetails,name='wastedetails'),

path('usertype/',views.usertype,name='usertype'),
path('logout/',views.logout,name='logout')
]