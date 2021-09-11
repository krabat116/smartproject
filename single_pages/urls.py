from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('generic/', views.generic),
    path('lang/', views.lang_view),
]