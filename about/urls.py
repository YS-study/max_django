from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
