# Generated by Django 3.1.4 on 2020-12-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20201221_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('treats', 'treats'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
