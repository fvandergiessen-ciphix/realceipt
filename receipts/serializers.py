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

class ReceiptItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptItem
        fields = ['id', 'product_name', 'product_price', 'receipt']

#    receipt = serializers.HyperlinkedRelatedField(
#        queryset = Receipt.objects.all(),
#        view_name = 'receipt_detail'
#   )

class AddReceiptSerializer(serializers.ModelSerializer):
    files = serializers.FileField()

    def save(self, **kwargs):
        receipt_id = self.context['receipt_id']
        files = self.validated_data['files']
        receipt_description = self.validated_data['receipt_description']

        try:
            receipt = Receipt.objects.get(receipt_id = receipt_id)
            receipt.receipt_description += receipt_description
            receipt.save()
        except Receipt.DoesNotExist:
            Receipt.objects.create(receipt_id = receipt_id, **self.validated_data)

    class Meta:
        model = Receipt
        fields = ['id', 'receipt_description','uploaded_at', 'files']

class ReceiptSerializer(serializers.ModelSerializer):
    files = ReceiptFileSerializer(many=True, read_only = True)
    items = ReceiptItemSerializer(many=True, read_only = True)

    class Meta:
        model = Receipt
        fields = ['id', 'receipt_description','uploaded_at', 'files','items'] #file werkt niet for some reason