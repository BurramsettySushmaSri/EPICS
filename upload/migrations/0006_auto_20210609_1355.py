# Generated by Django 3.0.8 on 2021-06-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Age',
            field=models.IntegerField(blank=True),
        ),
    ]
