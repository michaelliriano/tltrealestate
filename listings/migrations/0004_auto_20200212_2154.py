# Generated by Django 3.0.3 on 2020-02-12 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200211_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_published',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='is_sold',
            new_name='sold',
        ),
    ]