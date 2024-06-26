# Generated by Django 5.0.4 on 2024-04-18 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0003_receipt_receipt_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='receipt',
            name='file',
            field=models.FileField(default='-', upload_to='receipts/files'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receipt',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='receiptitem',
            name='receipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='receipts.receipt'),
        ),
        migrations.DeleteModel(
            name='ReceiptFile',
        ),
    ]
