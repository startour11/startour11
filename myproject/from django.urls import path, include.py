from django.urls import path, include
from myapp import views
urlpatterns=[
    path('home/',views.homeview.as_view()),
]

