from django.db import models



class Receipt(models.Model):
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

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)



