# Generated by Django 5.0.6 on 2024-06-03 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=50)),
                ('additional_details', models.TextField()),
                ('image1', models.ImageField(upload_to='products/')),
                ('image2', models.ImageField(upload_to='products/')),
                ('image3', models.ImageField(upload_to='products/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
        ),
    ]
