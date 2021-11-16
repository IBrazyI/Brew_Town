from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_products, name='products'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('management/', views.product_management, name='product_management'),
]