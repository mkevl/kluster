# Generated by Django 3.2.9 on 2021-11-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0006_auto_20211115_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceprovider',
            name='provider_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceprovider',
            name='provider_logo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
