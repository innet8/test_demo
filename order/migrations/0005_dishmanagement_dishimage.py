# Generated by Django 3.2.1 on 2023-12-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_remove_dishmanagement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishmanagement',
            name='Dishimage',
            field=models.ImageField(blank=True, null=True, upload_to='Dishimage/%Y/%m/%d/', verbose_name='菜品图片'),
        ),
    ]
