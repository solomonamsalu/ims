# Generated by Django 4.1 on 2022-09-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_remove_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='Abe', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='tefe', max_length=100),
            preserve_default=False,
        ),
    ]
