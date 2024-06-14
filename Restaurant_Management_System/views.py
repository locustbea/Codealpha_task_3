from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order, Table, InventoryItem
from .forms import OrderForm, MenuItemForm, TableForm, InventoryItemForm

def home(request):
    return render(request, 'management/home.html')

def menu_items(request):
    items = MenuItem.objects.all()
    return render(request, 'management/menu_items.html', {'items': items})

def create_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_items')
    else:
        form = MenuItemForm()
    return render(request, 'management/create_menu_item.html', {'form': form})

def orders(request):
    orders = Order.objects.all()
    return render(request, 'management/orders.html', {'orders': orders})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm()
    return render(request, 'management/create_order.html', {'form': form})

def tables(request):
    tables = Table.objects.all()
    return render(request, 'management/tables.html', {'tables': tables})

def create_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tables')
    else:
        form = TableForm()
    return render(request, 'management/create_table.html', {'form': form})

def inventory(request):
    items = InventoryItem.objects.all()
    return render(request, 'management/inventory.html', {'items': items})

def create_inventory_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = InventoryItemForm()
    return render(request, 'management/create_inventory_item.html', {'form': form})
