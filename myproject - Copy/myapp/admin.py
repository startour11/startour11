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
    pass
