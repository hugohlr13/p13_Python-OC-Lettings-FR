# Generated by Django 3.0 on 2024-03-13 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20240313_1602'),
        ('lettings', '0002_auto_20240313_1603'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
    ]