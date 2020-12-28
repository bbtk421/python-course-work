from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class MetaL:
        model = Product
        fields = '__all__'