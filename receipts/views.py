from django.shortcuts import render
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from rest_framework import status,viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet

from .models import Receipt,ReceiptItem
from .serializers import ReceiptSerializer,ReceiptItemSerializer, AddReceiptSerializer

def hello(request):
    return render(request, 'hello.html')


class ReceiptItemViewSet(ReadOnlyModelViewSet):
    queryset = ReceiptItem.objects.all()
    serializer_class = ReceiptItemSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    

class NewReceiptViewSet(CreateModelMixin, GenericViewSet):
    queryset = Receipt.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddReceiptSerializer
        return ReceiptSerializer
    
    def get_serializer_context(self):
        return {'receipt_id': self.kwargs['receipts_pk']}
    
    def get_serializer_context(self):
        return {'request': self.request}


class ReceiptViewSet(ReadOnlyModelViewSet): 
    queryset = Receipt.objects.all() 
    serializer_class = ReceiptSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}

