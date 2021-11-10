# Generated by Django 3.2.9 on 2021-11-10 19:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('company', 'company'), ('person', 'person')], max_length=40)),
                ('num_beneficiaries', models.PositiveIntegerField(default=0, help_text='Number of beneficiaries for the customer')),
                ('insurance_package', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customers', to='insurance.insurancepackage')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
