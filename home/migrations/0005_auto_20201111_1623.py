# Generated by Django 3.1.1 on 2020-11-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201111_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pppp',
            name='product_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]