from rest_framework import serializers
from receipts.models import ReceiptFile, Receipt,ReceiptItem
from django.shortcuts import render

class ReceiptFileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        receipt_id = self.context['receipt_id']
        return ReceiptFile.objects.create(receipt_id = receipt_id, **validated_data)

    class Meta:
        model = ReceiptFile
        fields = ['id', 'file']

class ReceiptSerializer(serializers.ModelSerializer):
    file = ReceiptFileSerializer(many=True, read_only = True)

    class Meta:
        model = Receipt
        fields = ['id', 'receipt_description','uploaded_at', 'file']

class ReceiptItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptItem
        fields = ['id', 'product_name', 'product_price', 'receipt']

#    receipt = serializers.HyperlinkedRelatedField(
#        queryset = Receipt.objects.all(),
#        view_name = 'receipt_detail'
#    )

