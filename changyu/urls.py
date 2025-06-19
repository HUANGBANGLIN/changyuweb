# changyu/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service', views.service, name='service'),
    path('projectshare', views.projectshare, name='projectshare'),
    path('csr', views.csr, name='csr'),
    path('contact', views.contact, name='contact'),

]
