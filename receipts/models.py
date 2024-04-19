from django.db import models
from uuid import uuid4

class Receipt(models.Model):
    id = models.AutoField(primary_key=True)
    receipt_description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads')

    def __str__(self) -> str:
        return self.receipt_description

class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name = 'items')
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str: 
        return self.product_name
    
#class Employee(models.Model):
#    first_name = models.CharField(max_length=255)
#    last_name = models.CharField(max_length=255)
#    job_title = models.CharField(max_length=255)


