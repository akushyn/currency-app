# Generated by Django 4.2 on 2023-05-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_exchangerate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]