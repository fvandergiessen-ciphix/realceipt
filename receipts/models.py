from django.db import models
from uuid import uuid4


class Receipt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    receipt_description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.receipt_description

class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name = 'items')
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str: 
        return self.product_name

class ReceiptFile(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='receipts/files')

