from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.about,name="about"),
    path('home/',views.home,name="home"),
    path('result/',views.result,name="result"),
    path('fertilizer/',views.fertilizer,name="fertilizer"),
    path('result2/',views.result2,name="result2"),
]
