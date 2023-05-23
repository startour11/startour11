from django.urls import path, include
from myapp import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView,    PasswordResetDoneView,  PasswordResetConfirmView,   PasswordResetCompleteView
urlpatterns=[
    path('home/',views.homeview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('boot/',views.bootview.as_view()),
    path('kboot/',views.kbootview.as_view()),
    path('renovat/',views.renovatview.as_view()),
    path('form/',views.formview.as_view()),
    path('tourandtravels/',views.tourandtravelsview),
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
    path('thankyou/<int:id>',views.thankyouview,name="thankyou"),
    path('insertabout/',views.insertabout),
    path('trip/',views.trip),
    path('searchresult/',views.searchview),
    path('mybookings/',views.mybookingview),
    path('edit/<int:id>',views.editview),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
    
]



