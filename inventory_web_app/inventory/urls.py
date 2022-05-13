from django.urls import path
from . import views
from .views import ProductCreateView, ProductEditView

urlpatterns = [
    path('', views.landing_page, name='base'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(), name='edit_product'),
    path('product/<int:pk>/delete', ProductCreateView.as_view(), name='create_product'),
]
