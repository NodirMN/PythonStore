# Generated by Django 4.1.7 on 2023-03-11 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='nameproduct',
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='name',
            new_name='namecategory',
        ),
    ]
