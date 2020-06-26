from django.urls import path

from TpFinalBioApp import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('map',views.map, name="Map"),
]