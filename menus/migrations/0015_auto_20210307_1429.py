# Generated by Django 3.1.5 on 2021-03-07 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0014_auto_20210307_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='menus.menuitem'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='type',
            field=models.CharField(choices=[('item', 'Item'), ('category', 'Category')], default='item', max_length=10),
        ),
    ]
