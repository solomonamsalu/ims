# Generated by Django 4.1 on 2022-08-23 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_item_sku_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='seling_price',
            new_name='selling_price',
        ),
    ]
