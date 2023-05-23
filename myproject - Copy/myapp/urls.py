from django.urls import path, include
from myapp import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns=[
    path('home/',views.homeview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('boot/',views.bootview.as_view()),
    path('kboot/',views.kbootview.as_view()),
    path('renovat/',views.renovatview.as_view()),
    path('form/',views.formview.as_view()),
    path('tourandtravels/',views.tourandtravelsview.as_view()),
    path('contact/',views.contactview.as_view()),
    path('insertcontact/',views.insertcontact),
     path('insertbooking/',views.insertbooking),
    path('aboutus/',views.aboutusview.as_view()),
    path('FAQs/',views.FAQsview),
    path('blogs/',views.blogview),
    path('blogsdetail/<int:id>',views.blogsdetail),
    path('Destinations/',views.Destinationsview),
    path('hotels/',views.Hotelsview),
    path('signup/',views.signupview),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"), 
    path('booking/',views.bookingview), 
    path('tour/',views.tourview),  
    path('tourdetail/<int:id>',views.tourdetail), 
    path('thankyou/',views.thankyouview),
]

