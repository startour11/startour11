from django.contrib import admin
from myapp.models import *
# Register your models here.

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('fullname','email','phone','message',)


@admin.register(blogs)
class blogsadmin(admin.ModelAdmin):
    pass
@admin.register(Hotels)
class hoteladmin(admin.ModelAdmin):
    pass
@admin.register(Touristplaces)
class Touristplaces(admin.ModelAdmin):
    pass
@admin.register(faqs)
class Faqadmin(admin.ModelAdmin):
    pass
@admin.register(tour)
class touradmin(admin.ModelAdmin):
    pass
@admin.register(booking)
class bookingadmin(admin.ModelAdmin):
    list_display=('FirstName','LastName','No_of_Children','ContactNumber','No_of_Adults','EmailId','CheckIn','Checkout','Tourtype','instructions','status')

@admin.register(internationalpackage)
class internationalpackageadmin(admin.ModelAdmin):
    pass

@admin.register(about)
class aboutadmin(admin.ModelAdmin):
    list_display=('name','email','phone','interested_in','no_of_person',)


@admin.register(Ordernow)
class Ordernowadmin(admin.ModelAdmin):
    pass

