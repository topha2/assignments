from django.urls import path
from . import views

urlpatterns = [
   
     path('',views.home, name="home"),
    path('base/',views.base, name="base"),
    path('contact/',views.contact, name="contact"),
    path('table/', views.table, name="table"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),



]