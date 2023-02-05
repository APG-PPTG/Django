# Generated by Django 4.0.6 on 2023-02-04 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_contactinfo1_person_student1_teacher1_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=22)),
                ('f2', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Parent2',
            fields=[
                ('f3', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('f4', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parent2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='testapp.parent2')),
                ('parent1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.parent1')),
                ('f5', models.CharField(max_length=22)),
                ('f6', models.CharField(max_length=22)),
            ],
            bases=('testapp.parent1', 'testapp.parent2'),
        ),
    ]