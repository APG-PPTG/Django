# Generated by Django 4.0.6 on 2023-02-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=10)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=30)),
            ],
        ),
    ]
