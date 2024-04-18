from django.shortcuts import render
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from rest_framework import status,viewsets,mixins
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Receipt,ReceiptItem,Employee,ReceiptFile
from .serializers import ReceiptSerializer,ReceiptFileSerializer,ReceiptItemSerializer

def hello(request):
    return render(request, 'hello.html')

#Viewset
class ReceiptItemViewSet(ModelViewSet):
    queryset = ReceiptItem.objects.all()
    serializer_class = ReceiptItemSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
class ReceiptFileViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptFileSerializer

    def get_serializer_context(self):
        return {'receipt_id': self.kwargs['receipts_pk']}
    
    def get_queryset(self):
        return ReceiptFile.objects.filter(receipt_id = self.kwargs['receipts_pk'])
    
class ReceiptViewSet(ReadOnlyModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
class NewReceiptViewSet(ModelViewSet):
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
    
