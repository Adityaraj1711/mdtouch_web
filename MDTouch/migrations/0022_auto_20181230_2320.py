# Generated by Django 2.0.9 on 2018-12-30 17:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MDTouch', '0021_auto_20181225_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalFacilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilities', models.CharField(default='', max_length=200)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MDTouch.Hospital')),
            ],
        ),
        migrations.AlterField(
            model_name='ambulancebilling',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 23, 20, 11, 47233)),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 23, 20, 11, 46235)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MDTouch.Qualification'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MDTouch.Specialization'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 23, 20, 11, 46235)),
        ),
    ]
