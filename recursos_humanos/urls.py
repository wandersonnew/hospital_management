from django.urls import path

from . import views

urlpatterns = [
    path('recursos_humanos', views.recursos_humanos),
    path('authorized', views.authorized),
    path('', views.home),
]