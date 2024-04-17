from django.shortcuts import render
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from .models import Receipt,ReceiptItem,Employee,ReceiptFile
from .serializers import ReceiptSerializer,ReceiptFileSerializer,ReceiptItemSerializer

def hello(request):
    return render(request, 'hello.html')

def uploadreceipts(request):
    return render(request, 'upload_receipts.html')

def viewreceipts(request):
    return render(request, 'view_receipts.html')

#Viewset
class ReceiptItemViewSet(ModelViewSet):
    queryset = ReceiptItem.objects.all()
    serializer_class = ReceiptItemSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
#Viewset
class ReceiptViewSet(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}

#class ReceiptItemDetail(RetrieveUpdateDestroyAPIView):
#    lookup_field = 'id'

#@api_view
#def receipt_detail(request, pk):
#    return Response('ok')

#class ReceiptList(ListCreateAPIView):
#    queryset = Receipt.objects.annotate(
#        receipt_count = Count('receiptitem')).all()
#    serializer_class = ReceiptSerializer
    
class ReceiptFileViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptFileSerializer
    def get_queryset(self):
        return ReceiptFile.objects.all()#.filter(receipt_id=self.kwargs['receipt_pk'])