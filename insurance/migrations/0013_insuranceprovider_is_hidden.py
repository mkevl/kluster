# Generated by Django 3.2.9 on 2021-11-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0012_insurancepackage_is_best_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='insuranceprovider',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]