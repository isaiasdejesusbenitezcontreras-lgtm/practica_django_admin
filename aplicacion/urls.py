from django.urls import path
from . import views

urlpatterns = [
    path('', views.portal_noticias, name='portal_noticias'),
]