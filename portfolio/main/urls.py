from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('downloadcv/', download_cv, name='download_cv'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]
