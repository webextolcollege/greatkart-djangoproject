# Generated by Django 3.1 on 2024-11-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_variation_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='created_date',
            field=models.DateTimeField(default=True),
        ),
    ]