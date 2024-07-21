from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
urlpatterns = [
    path('',receipt_home, name='login_receipt'),
    path('login/', login_receipt, name='login_receipt'),
    path('register/', register_receipt, name='register_receipt'),

    path('logout/', custom_logout, name='logout'),

    path('receipts/', receipts, name='receipts'),
    path('update_receipt/<id>/', update_receipt, name='update_receipt'),
    path('delete_receipt/<id>/', delete_receipt, name='delete_receipt'),
    path('pdf/', pdf, name='pdf'),
    # Add other paths as needed
]


