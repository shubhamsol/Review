from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='product_home'),
    path('product_page/',views.product_page,name='product_page'),
]