# Generated by Django 3.1.5 on 2021-03-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0009_auto_20210224_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='type',
            field=models.CharField(choices=[('item', 'Item'), ('category', 'Category')], default='item', max_length=10),
        ),
    ]
