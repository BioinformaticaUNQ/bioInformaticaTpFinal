from django.urls import path

from TpFinalBioApp import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('map/<int:upload_id>/', views.map, name="Map"),
    path('upload',views.upload, name="Upload"),
    path('uploadedsecuence', views.uploaded_secuence, name="UploadedSecuence"),
]