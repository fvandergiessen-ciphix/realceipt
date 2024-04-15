from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets

from receipts.models import Receipt,ReceiptItem,Employee,ReceiptFile
from .serializers import ReceiptSerializer,ReceiptFileSerializer,ReceiptItemSerializer

def hello(request):
    return render(request, 'hello.html')

def uploadreceipts(request):
    return render(request, 'upload_receipts.html')

def viewreceipts(request):
    return render(request, 'view_receipts.html')

@api_view()
def receiptitems_list(request):
    queryset = ReceiptItem.objects.all()
    serializer = ReceiptItemSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def receiptitems_detail(request, id):
    receipt = get_object_or_404(ReceiptItem, pk=id)
    serializer = ReceiptItemSerializer(receipt)
    return Response(serializer.data)

#class ReceiptFileViewSet(viewsets.ModelViewSet):
#    serializer_class = ReceiptFileSerializer
#    def get_queryset(self):
#        return ReceiptFile.objects.filter(file_id=self.kwargs['receipt_pk'])