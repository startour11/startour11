import http
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from myapp.forms import *
from django.contrib.auth import login
import razorpay
from django.http import HttpResponse


from django.contrib import messages
# Create your views here.
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import razorpay

from django.http import HttpResponse


def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        orderid=request.POST.get("provider_order_id")
        bookingid=request.POST.get("bookingid")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": float(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Ordernow.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order['id'],bookingid_id=bookingid
        )
        order.save()
        return render(
            request,
            "payment.html",
            {
                "callback_url": "http://127.0.0.1:8000/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )
    return render(request, "payment.html")


@csrf_exempt
def callback(request):
    
    razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    #    return client.utility.verify_payment_signature(response_data)

    if request.method == "POST":
        try:
            payment_id = request.POST.get("razorpay_payment_id", "")
            provider_order_id = request.POST.get("razorpay_order_id", "")
            signature_id = request.POST.get("razorpay_signature", "")
            params_dict={
                'razorpay_order_id':provider_order_id,
                'razorpay_payment_id':payment_id,
                'razorpay_signature':signature_id

            }
            print(params_dict)
            try:
                order = Ordernow.objects.get(provider_order_id=provider_order_id)
            except:
                return HttpResponse("505 not found inner")
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()
            
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            
            if result==True:
                amount=int(order.amount)
                
                try:
                   
                    '''res=razorpay_client.payment.capture(payment_id,{
                        "amount" : amount,
                        "currency" : "INR"
                        })
                    print(res)'''
                    order.status=PaymentStatus.SUCCESS
                    order.save()
                    return render(request, "sucess.html")
                except:
                   
                    order.status=PaymentStatus.FAILURE
                    order.save()
                    return render(request, "failure.html")
            else:
                
                order.status=PaymentStatus.FAILURE
                order.save()
                return render(request, "failure.html")
        except:
            return HttpResponse("505 not found here")
        


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
def tourandtravelsview(request):
    t=internationalpackage.objects.all()[:3]
    return render(request,"tourandtravels.html",{'t':t})
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

def insertabout(request):
    if request.method=='POST':
        form=aboutform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent." )
            return redirect('/aboutus/')
    else:
        form=aboutform()
    return render(request,"aboutus.html",{'form':form})

def trip(request):
    if request.method=='POST':
        form=trip(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent." )
            return redirect('/trip/')
    else:
        form=trip()
    return render(request,"trip.html",{'form':form})

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

def mybookingview(request):
    m=booking.objects.filter(userid_id=request.user)
    return render(request,"mybooking.html",{'m':m})

def editview(request,id):
    o=booking.objects.get(id=id)
    o.status='Cancel'
    o.save()
    return redirect('/mybookings/')

def insertbooking(request):
    if request.method=='POST':
        form=bookingform(request.POST)
        if form.is_valid():
            obj=form.save()
            id=obj.pk
            return redirect('thankyou',id=id)
    else:
        form=bookingform()
    return render(request,"booking.html",{'form':form})


def tourdetail(request,id):
    b=tour.objects.get(id=id)
    return render(request,"tourdetail.html",{'b':b})

def bookingview(request):
    t=tour.objects.all()
    return render(request,"booking.html",{'t':t})
def thankyouview(request,id):
    i=booking.objects.get(id=id)
    return render(request,"thankyou.html",{'i':i})

def searchview(request):
    qc=request.GET['qcity']
    v=tour.objects.filter(title__icontains=qc,description__icontains=qc)
    return render(request,"search.html",{'v':v})

def viewbookingview(request,id):
    book=booking.objects.filter(userid_id=request.user.id)
    return render(request,'viewbooking.html',{'book':book})

