# Generated by Django 3.2.13 on 2023-01-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=300)),
                ('short_url', models.CharField(max_length=200)),
            ],
        ),
    ]
