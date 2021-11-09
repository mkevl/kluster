# Generated by Django 3.2.9 on 2021-11-09 20:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_alter_insuranceprovider_price_last_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insuranceprovider',
            name='price_last_updated_at',
        ),
        migrations.RemoveField(
            model_name='insuranceprovider',
            name='price_per_month',
        ),
        migrations.CreateModel(
            name='InsurancePackage',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price_per_month', models.DecimalField(decimal_places=2, max_digits=12)),
                ('price_last_updated_at', models.DateTimeField(blank=True)),
                ('insurance_type', models.CharField(choices=[('personal', 'personal'), ('company', 'company')], max_length=20)),
                ('package_type', models.CharField(choices=[('minimal', 'minimal'), ('basic', 'basic'), ('improved', 'improved')], max_length=20)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='insurance.insuranceprovider')),
            ],
        ),
    ]