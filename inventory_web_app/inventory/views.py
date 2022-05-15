from django.contrib import messages
from django.forms import formset_factory
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from inventory.forms import ProductFormSet, ProductForm
from inventory.models import Product, Shipment, ShipmentItem


def landing_page(request):
    """View function for inventory landing page."""

    # Render the HTML template base.html with the data in the context variable
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
    paginate_by = 10
    template_name = 'view_products.html'
    ordering = ['name']


class CreateShipmentView(View):
    template_name = 'create_shipment.html'

    def products_to_formset(self, products):
        """
        Return the work lists associated to the work list items we want to display. We display entered work list items
        if is_entered is True, else unentered work list items.
        """
        WorkListItemFormSet = formset_factory(form=ProductForm,
                                              formset=ProductFormSet,
                                              extra=0)
        return WorkListItemFormSet(initial=ProductFormSet.initialize_data(products))

    def context(self, request):
        products = Product.objects.all().order_by('name')
        formset = self.products_to_formset(products)
        context = {
            'formset': formset
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.context(request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if self.create_shipment_and_update_inventory(request.POST):
            messages.add_message(request, messages.SUCCESS, 'Shipment created!', extra_tags='success')
        else:
            messages.add_message(request, messages.WARNING,
                                 'Shipment not created. Double check that the values entered are valid.',
                                 extra_tags='warning')

        context = self.context(request)
        return render(request, self.template_name, context)

    def create_shipment_and_update_inventory(self, post_data: dict) -> bool:
        """
        Update the products' quantity values for the products to be shipped, specified by the user.  If the quantity
        specified is negative or if there is not enough product left in stock for the user to ship, return False.
        Otherwise, return True.
        """
        num_items = int(post_data['form-TOTAL_FORMS'])
        products_to_be_shipped = []

        for i in range(num_items):
            quantity_to_ship = int(post_data[f'form-{i}-quantity_to_ship'])
            product_id = post_data[f'form-{i}-product_id']
            product = Product.objects.get(id=product_id)

            if quantity_to_ship < 0 or product.quantity < quantity_to_ship:
                return False

            if quantity_to_ship > 0:
                products_to_be_shipped.append((product_id, quantity_to_ship))

        shipment = Shipment.create_shipment(post_data['shipment_name'])
        for product_id, quantity_to_ship in products_to_be_shipped:
            product = Product.objects.get(id=product_id)
            product.update_quantity(quantity_to_ship)
            ShipmentItem.create_shipment_item(shipment, product.name, quantity_to_ship)

        return True


class ShipmentHistoryView(ListView):
    model = Shipment
    template_name = 'shipment_history.html'
    paginate_by = 10
    ordering = ['-created_at']