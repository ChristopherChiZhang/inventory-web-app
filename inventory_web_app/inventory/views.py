from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from inventory.models import Product


def landing_page(request):
    """View function for inventory landing page."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'base.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'sku', 'description', 'quantity']
    template_name = 'create_product.html'
    success_url = reverse_lazy('view_products')


class ProductEditView(UpdateView):
    model = Product
    fields = ['name', 'sku', 'description', 'quantity']
    template_name = 'edit_product.html'
    success_url = reverse_lazy('view_products')


class ProductDeleteView(DeleteView):
    model = Product
    fields = ['name', 'sku', 'description', 'quantity']
    template_name = 'delete_product.html'
    success_url = reverse_lazy('view_products')


class ProductView(ListView):
    model = Product
    paginate_by = 100
    template_name = 'view_products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context
