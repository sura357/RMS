# Generated by Django 3.2.15 on 2022-09-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rehabilitator',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('professional1', models.CharField(max_length=20)),
                ('professional2', models.CharField(max_length=20)),
                ('phonenumber', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=40)),
                ('remark', models.CharField(max_length=200)),
            ],
        ),
    ]