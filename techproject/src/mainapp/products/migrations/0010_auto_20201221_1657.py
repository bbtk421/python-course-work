# Generated by Django 3.1.4 on 2020-12-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20201219_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('treats', 'treats')], max_length=60),
        ),
    ]