from django.shortcuts import render
items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 599.99},
    {"id": 3, "name": "Headphones", "price": 199.99},
    {"id": 4, "name": "Smart Watch", "price": 149.99},
]
def item_list(request):
    return render(request, 'shop/item_list.html', {'items': items})

def item_detail(request, item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    return render(request, 'shop/item_detail.html', {'item': item})

# Create your views here.
