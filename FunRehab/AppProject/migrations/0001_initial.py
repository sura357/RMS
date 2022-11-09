# Generated by Django 3.2.15 on 2022-08-28 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KinectStatus',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateField(max_length=8)),
                ('useful_life', models.PositiveIntegerField()),
                ('rent', models.PositiveIntegerField()),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('birthday', models.DateField(max_length=8)),
                ('phonenumber', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=40)),
                ('remark', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20)),
                ('cSex', models.CharField(default='M', max_length=2)),
                ('cBirthday', models.DateField()),
                ('cEmail', models.EmailField(blank=True, default='', max_length=100)),
                ('cPhone', models.CharField(blank=True, default='', max_length=50)),
                ('cAddr', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RentalRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startingdate', models.DateField()),
                ('duration', models.PositiveIntegerField()),
                ('status', models.IntegerField(default=1)),
                ('kID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.kinectstatus')),
                ('pID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.patient')),
            ],
            options={
                'unique_together': {('kID', 'pID')},
            },
        ),
    ]
