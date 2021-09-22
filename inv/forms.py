from django import forms
from .models import Products


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'quantity', 'category')

