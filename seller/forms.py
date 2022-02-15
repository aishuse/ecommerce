from django import forms
from .models import Product, ProductStock


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'price', 'details', 'image', 'category']
        widgets = {

            'name': forms.TextInput(attrs={"class": "form-control"}),
            'brand': forms.TextInput(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'details': forms.Textarea(attrs={"class": "form-control"}),

        }


class ProductStockForm(forms.ModelForm):
    class Meta:
        model = ProductStock
        fields = ['stock_available', 'product']
        widgets = {
            'stock_available': forms.NumberInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user') # Important to do this
        # If you dont, calling super will fail because the init does
        # not expect, user among the fields.
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(user=user)