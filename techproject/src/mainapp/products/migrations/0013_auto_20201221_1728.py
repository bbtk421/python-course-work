# Generated by Django 3.1.4 on 2020-12-22 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20201221_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
