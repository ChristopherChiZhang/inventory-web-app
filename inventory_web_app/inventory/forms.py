from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    sku = forms.CharField(required=True)
    product_id = forms.IntegerField(required=True, widget=forms.HiddenInput())
    quantity_available = forms.IntegerField(required=True, initial=0)
    quantity_to_ship = forms.IntegerField(required=True, initial=0)


class ProductFormSet(forms.BaseFormSet):

    @classmethod
    def initialize_data(cls, products):
        return [{'name': product.name,
                 'sku': product.sku,
                 'product_id': product.id,
                 'quantity_available': product.quantity,
                 'quantity_to_ship': 0} for product in products]
