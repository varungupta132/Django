"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from receipt.views import *
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from api import urls
from receipt import urls

urlpatterns = [
    path('',home),
    
    # path('gen/',base),

    # path('receipts/', receipts, name='receipts'),
    # path('update/<int:id>/', update_receipt, name='update_receipt'),
    # path('delete/<int:id>/', delete_receipt, name='delete_receipt'),
    # path('login/', login_receipt, name='login_receipt'),
    # path('register/',register_receipt, name='register_receipt'),
    # path('logout/', custom_logout, name='custom_logout'),
    # path('pdf/', pdf, name='pdf'),        
    
    
    
    
    
    path("successfully",success_page,name="success_page"),
    
    path('receipes',receipes),
    
    path('login/',login_page,name="login"),

    path('logout/',logout_page),
    
    path('regester/',regester_page),
    
    path('admin/', admin.site.urls),
    
    path('update-receipes/<id>/',receipe_update,name="receipe_update"),
    
    path('delete-receipes/<id>/',receipe_delete,name="receipe_delete"),
    
    path('send_email/',send_email, name='send_email'),
    
    path('api/v1/',include('api.urls')),
    
    
    path("gen/",include('receipt.urls'))
    
    

]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
urlpatterns += staticfiles_urlpatterns()
