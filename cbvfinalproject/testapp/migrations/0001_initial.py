# Generated by Django 4.0.6 on 2023-01-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('taste', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('price', models.FloatField()),
            ],
        ),
    ]
