# Generated by Django 3.0.3 on 2020-02-11 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_is_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]