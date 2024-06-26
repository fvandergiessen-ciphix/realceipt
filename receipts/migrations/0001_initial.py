# Generated by Django 5.0.4 on 2024-04-19 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receipt_description', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='receipts.receipt')),
            ],
        ),
    ]
