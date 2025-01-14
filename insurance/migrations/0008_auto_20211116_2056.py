# Generated by Django 3.2.9 on 2021-11-16 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0007_auto_20211116_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceprovider',
            name='provider_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceprovider',
            name='provider_logo',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
