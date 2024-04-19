from rest_framework import serializers
from receipts.models import  Receipt,ReceiptItem
from django.shortcuts import render

class ReceiptItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptItem
        fields = ['id', 'product_name', 'product_price', 'receipt']


class AddReceiptSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        receipt_description = self.validated_data['receipt_description']
        file = self.validated_data['file']
        #files = self.validated_data.pop('files', None)
        
        self.instance = Receipt.objects.create(**self.validated_data)
        #self.instance.files.set(self.validated_data[files])
        return self.instance
    
    def set_value(self, dictionary, keys, value):
        return super().set_value(dictionary, keys, value)
    
    class Meta:
        model = Receipt
        fields = ['id', 'receipt_description','uploaded_at', 'file']


class ReceiptSerializer(serializers.ModelSerializer):
    items = ReceiptItemSerializer(many=True, read_only = True)

    class Meta:
        model = Receipt
        fields = ['id', 'receipt_description','uploaded_at','file','items'] 