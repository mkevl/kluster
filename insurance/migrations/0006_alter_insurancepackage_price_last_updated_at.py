# Generated by Django 3.2.9 on 2021-11-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0005_auto_20211109_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancepackage',
            name='price_last_updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
