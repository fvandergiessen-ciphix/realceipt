from django.db import models


class Receipt(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)

class ReceiptFile(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    file = models.FileField(upload_to='receipts/files')

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)



