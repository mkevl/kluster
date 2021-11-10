# Generated by Django 3.2.9 on 2021-11-10 21:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancepackage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insurancepackage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
