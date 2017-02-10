from django import forms

from ordenes.models import Orden
from website.models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('direccion',)
