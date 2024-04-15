from rest_framework import serializers
from receipts.models import ReceiptFile, Receipt,ReceiptItem

class ReceiptSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    uploaded_at = serializers.DateTimeField()

class ReceiptItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=255)
    product_price = serializers.DecimalField(max_digits=6,decimal_places=2)
    receipt = ReceiptSerializer()

class ReceiptFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptFile
        fields = ['id', 'file']