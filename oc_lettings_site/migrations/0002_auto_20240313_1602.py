# Generated by Django 3.0 on 2024-03-13 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letting',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='oc_lettings_site.Address'),
        ),
    ]
