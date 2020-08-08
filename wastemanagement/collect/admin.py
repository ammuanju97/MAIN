from django.contrib import admin
from .models import AddProduct, CollectDetails, BookForm, Payment, SellPayment
# Register your models here.


# from django.contrib import admin
# from .models import AddProduct
# Register your models here.
admin.site.register(AddProduct)

admin.site.register(CollectDetails)

admin.site.register(BookForm)

admin.site.register(Payment)

admin.site.register(SellPayment)