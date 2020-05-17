from django . urls import path
from . import views

urlpatterns = [

path('adminhome/',views.adminhome, name='adminhome'),
path('category/',views.category, name='category'),
path('addcategory/',views.addcategory, name='addcategory'),
path('adminhome1/',views.adminhome1, name='adminhome1'),
path('viewuserlist/',views.viewuserlist,name='viewuserlist'),
path('addadmin/',views.addadmin,name='addadmin'),
path('addrecycle/',views.addrecycle,name='addrecycle'),
path('category1/',views.category1,name='category1'),
path('viewcollect/',views.viewcollect,name='viewcollect'),
path('approvcollect/',views.approvcollect,name='approvcollect')
]