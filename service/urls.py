from django.urls import path
from service import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('', views.index, name='index'),
]
