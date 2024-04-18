# Generated by Django 5.0.4 on 2024-04-18 11:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0003_receipt_receipt_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='receiptfile',
            name='receipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='receipts.receipt'),
        ),
        migrations.AlterField(
            model_name='receiptitem',
            name='receipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='receipts.receipt'),
        ),
    ]
