# Generated by Django 3.1 on 2020-08-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_Id',
            field=models.IntegerField(default=''),
        ),
    ]
