# Generated by Django 4.1 on 2022-08-28 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_store_company'),
        ('inventory', '0003_alter_supplier_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.store'),
        ),
    ]
