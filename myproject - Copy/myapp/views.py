import http
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from myapp.forms import *
from django.contrib.auth import login
# Create your views here.

class homeview(TemplateView):
    template_name="home.html"
class aboutview(TemplateView):
    template_name="about.html"
class bootview(TemplateView):
    template_name="boot.html"
class kbootview(TemplateView):
    template_name="kboot.html"
class renovatview(TemplateView):
    template_name="renovat.html"
class formview(TemplateView):
    template_name="form.html"
class tourandtravelsview(TemplateView):
    template_name="tourandtravels.html"
class contactview(TemplateView):
    template_name="contact.html"
class aboutusview(TemplateView):
    template_name="aboutus.html"
class shopview(TemplateView):
    template_name="shop.html"

def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=contactform()
    return render(request,"contact.html",{'form':form})

def signupview(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/blogs')
    else:
       form=signupform()
    return render(request,"registration/signup.html",{'form':form}) 
 
def blogview(request):
    blg=blogs.objects.all()
    return render(request,"blog.html",{'blg':blg})

def blogsdetail(request,id):
    blg=blogs.objects.get(id=id)
    return render(request,"blogsdetail.html",{'blg':blg})
    
def FAQsview(request):
    f=faqs.objects.all()
    return render(request,"FAQs.html",{'f':f})


def Destinationsview(request):
    d=Touristplaces.objects.all()
    return render(request,"Destination.html",{'d':d})

def Hotelsview(request):
    h=Hotels.objects.all()
    return render(request,"Hotels.html",{'h':h})

def tourview(request):
    t=tour.objects.all()
    return render(request,"tour.html",{'t':t})

def insertbooking(request):
    if request.method=='POST':
        form=bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thankyou/')
    else:
        form=bookingform()
    return render(request,"booking.html",{'form':form})


def tourdetail(request,id):
    b=tour.objects.get(id=id)
    return render(request,"tourdetail.html",{'b':b})

def bookingview(request):
    t=tour.objects.all()
    return render(request,"booking.html",{'t':t})
def thankyouview(request):
    return render(request,"thankyou.html")