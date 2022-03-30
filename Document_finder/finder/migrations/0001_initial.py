# Generated by Django 4.0.3 on 2022-03-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('spec', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
