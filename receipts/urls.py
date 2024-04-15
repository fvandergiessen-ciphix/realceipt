from django.urls import path
from . import views

urlpatterns = [
    path('homepage/',views.hello),
    path('receipts/',views.receiptitems_list),
    path('receipts/<int:id>/',views.receiptitems_detail),
]