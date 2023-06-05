"""
URL configuration for ombor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Asosiy.views import *
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('bolim/', bolimlar),
    path('client/', client),
    path('client_update/', client_update),
    path('product_update/', product_update),
    path('product/', products),
    path('stats/', stats),
    path('logout/', logout1),
    path('product_delete/<int:pk>/', MahsulotOchirView.as_view()),
    path('product_edit/<int:pk>/', MahsulotEditView.as_view()),
    path('client_edit/<int:pk>/', MijozEditView.as_view()),
    path('client_delete/<int:pk>/', MijozDeleteView.as_view()),

]
