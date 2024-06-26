from django.urls import path
from .views import webcam_view

from . import views

app_name = 'imageupload'
urlpatterns = [
    #path('', views.ImageUploadView.as_view(), name='upload'),
    path('upload/', views.image_upload, name='upload'),
    path('index', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('menu/', views.menu, name='menu'),
    path('menu/historial', views.historial, name='historial'),
    path('menu/info', views.info, name='info'),
    path('webcam/', webcam_view, name='webcam'),
    path('logout/', views.logout_view, name='logout'),
    path('rekognition/', views.rekognition_view, name='rekognition'),
    path('rekognition_historial/<str:foto>', views.rekognition_historial, name='rekognition_historial'),
    path('reconocimiento_facial/', views.reconocimiento_facial, name='reconocimiento_facial')
]