# Generated by Django 4.0.3 on 2022-03-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_alter_treatment_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.TextField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Third_gender', 'Third_gender')], null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='dosage_per_day',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)], null=True),
        ),
    ]
