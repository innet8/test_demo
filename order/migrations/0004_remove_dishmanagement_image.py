# Generated by Django 3.2.1 on 2023-12-18 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_dishmanagement_dishclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishmanagement',
            name='image',
        ),
    ]
