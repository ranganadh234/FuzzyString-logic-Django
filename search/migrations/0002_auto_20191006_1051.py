# Generated by Django 2.2.6 on 2019-10-06 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordmodel',
            old_name='rank',
            new_name='frequency',
        ),
    ]