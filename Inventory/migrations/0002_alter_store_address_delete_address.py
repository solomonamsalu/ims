# Generated by Django 4.1 on 2022-08-22 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('Sales', '0002_alter_customer_address'),
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.address'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
