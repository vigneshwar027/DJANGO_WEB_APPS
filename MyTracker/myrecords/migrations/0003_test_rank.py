# Generated by Django 4.0.3 on 2022-03-26 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrecords', '0002_remove_test_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]