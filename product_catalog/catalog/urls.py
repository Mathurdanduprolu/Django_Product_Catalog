from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings  # Import settings

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]