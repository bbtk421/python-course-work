# Generated by Django 3.1.4 on 2020-12-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20201221_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
