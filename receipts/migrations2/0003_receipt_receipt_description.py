# Generated by Django 5.0.4 on 2024-04-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_receiptfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='receipt_description',
            field=models.CharField(default='Receipt', max_length=255),
            preserve_default=False,
        ),
    ]
