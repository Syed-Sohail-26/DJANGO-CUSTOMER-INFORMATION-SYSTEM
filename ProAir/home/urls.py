from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [

    path('',views.homepage),
    path('customers/',views.disp_cust),
    path('customer/',views.login),
    path('save/',views.save),
    path('cust_delete/<int:id>/',views.delete),
    path('cust_update/<int:id>/',views.update),
    path('update/',views.update_result),
    path('login/',views.login),
    path('loginprocess/',views.loginprocess),
    path('search/',views.search),
    path('serprocess/',views.serprocess),


]