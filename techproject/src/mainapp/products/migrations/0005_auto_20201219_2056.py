# Generated by Django 3.1.4 on 2020-12-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201219_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]