from django import forms
from .models import Cart

class Cart_Form(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = []

