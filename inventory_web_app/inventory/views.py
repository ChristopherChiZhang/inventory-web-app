from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from inventory.models import Product


def landing_page(request):
    """View function for inventory landing page."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'base.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'sku', 'description', 'quantity']


class ProductEditView(UpdateView):
    model = Product
    fields = ['name', 'sku', 'description', 'quantity']


class ProductDeleteView(DeleteView):
    model = Product
    fields = ['name', 'sku', 'description', 'quantity']
