# Generated by Django 3.2.15 on 2022-09-21 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProject', '0002_rehabilitator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GameSample',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=75)),
                ('video_file', models.CharField(max_length=75, null=True)),
                ('standard_file', models.CharField(max_length=75, null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.gamesample')),
            ],
        ),
        migrations.CreateModel(
            name='PlanSetDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.PositiveIntegerField()),
                ('times', models.PositiveIntegerField()),
                ('breadtime', models.PositiveIntegerField()),
                ('ontop_duration', models.PositiveIntegerField(null=True)),
                ('type', models.PositiveIntegerField()),
                ('motion_time', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='kinectstatus',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthday',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='rehabilitator',
            name='email',
            field=models.EmailField(max_length=40),
        ),
        migrations.AlterField(
            model_name='rentalrecords',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rentalrecords',
            name='startingdate',
            field=models.DateField(max_length=8),
        ),
        migrations.CreateModel(
            name='RehubRecord',
            fields=[
                ('sdID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AppProject.plansetdetail')),
                ('accuracy', models.PositiveIntegerField()),
                ('times', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('progress', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SetID', models.DateField(max_length=8)),
                ('order', models.PositiveIntegerField()),
                ('mID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.motion')),
                ('sdID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.plansetdetail')),
            ],
            options={
                'unique_together': {('SetID', 'order')},
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('planID', models.PositiveIntegerField()),
                ('creating_date', models.DateField(max_length=14)),
                ('setID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.planset')),
            ],
            options={
                'unique_together': {('id', 'setID')},
            },
        ),
        migrations.CreateModel(
            name='PlanSetMotion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.motion')),
                ('setID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.plansetdetail')),
            ],
            options={
                'unique_together': {('setID', 'mID')},
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creating_date', models.DateField(max_length=16)),
                ('disease', models.CharField(max_length=30)),
                ('symptom', models.CharField(max_length=40)),
                ('status', models.PositiveIntegerField()),
                ('remark', models.CharField(max_length=200, null=True)),
                ('pID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.patient')),
                ('planID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.plan')),
                ('rID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.rehabilitator')),
            ],
            options={
                'unique_together': {('rID', 'pID', 'planID')},
            },
        ),
        migrations.CreateModel(
            name='FitDisease',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.disease')),
                ('mID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.motion')),
            ],
            options={
                'unique_together': {('mID', 'dID')},
            },
        ),
        migrations.CreateModel(
            name='ContactRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('send_time', models.DateField(max_length=14)),
                ('content', models.CharField(max_length=200)),
                ('pID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.patient')),
                ('rID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.rehabilitator')),
            ],
            options={
                'unique_together': {('rID', 'pID')},
            },
        ),
    ]
