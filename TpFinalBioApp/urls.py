from django.conf import settings
from django.urls import path
from django.conf.urls.static import static


from TpFinalBioApp import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('map/<int:upload_id>/', views.map, name="Map"),
    path('upload',views.upload, name="Upload"),
    path('uploadedsecuence', views.uploaded_secuence, name="UploadedSecuence"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)