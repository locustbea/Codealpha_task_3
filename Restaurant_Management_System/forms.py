from django import forms
from .models import MenuItem, Order, Table, InventoryItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table', 'items']

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'capacity']

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity']
