# Generated by Django 4.2 on 2025-02-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_transaction_id_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
