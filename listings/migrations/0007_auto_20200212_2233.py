# Generated by Django 3.0.3 on 2020-02-12 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20200212_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='active',
            new_name='is_active',
        ),
    ]
