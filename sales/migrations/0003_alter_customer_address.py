# Generated by Django 4.1 on 2022-08-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_remove_customer_email_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(),
        ),
    ]
