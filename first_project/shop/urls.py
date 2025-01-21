from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.item_list, name = 'item_list'),
    path('<int:item_id>/', views.item_detail, name='item_detail')
]