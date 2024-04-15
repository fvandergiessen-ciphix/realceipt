from rest_framework import serializers
from receipts.models import ReceiptFile, Receipt,ReceiptItem

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['id', 'uploaded_at']

class ReceiptItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptItem
        fields = ['id', 'product_name', 'product_price', 'receipt']

#    receipt = serializers.HyperlinkedRelatedField(
#        queryset = Receipt.objects.all(),
#        view_name = 'receipt_detail'
#    )

class ReceiptFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptFile
        fields = ['id', 'file']