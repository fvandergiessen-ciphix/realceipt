from django.urls import path
from . import views

urlpatterns = [
    path('homepage/',views.hello),
    path('receiptitems/',views.receiptitems_list),
    path('receiptitems/<int:id>/',views.receiptitems_detail),
    path('receiptdetails/<int:pk>/',views.receipt_detail, name='receipt_detail'),
]