from django.urls import path
from . import views
from .views import ProductCreateView, ProductEditView, ProductDeleteView, ProductView, CreateShipmentView

urlpatterns = [
    path('', views.landing_page, name='base'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('shipment/create/', CreateShipmentView.as_view(), name='create_shipment'),
    path('products/view/', ProductView.as_view(), name='view_products'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(), name='edit_product'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='delete_product'),
]
