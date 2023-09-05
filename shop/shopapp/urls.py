from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.get_orders, name='orders_list'),
    path('orders/<int:order_id>/', views.get_order, name='order_details'),
    path('ordered-products/', views.get_ordered_products, name='ordered_products'),
    path('client/', views.client_form, name='client'),
    path('product/', views.product_form, name='product'),
    path('order/', views.order_form, name='order'),
    path('index', views.index, name='index'),
]
