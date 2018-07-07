# Generated by Django 2.0.6 on 2018-07-07 01:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25)),
                ('relationshipToHead', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=6)),
                ('age', models.PositiveIntegerField()),
                ('Mother', models.CharField(max_length=25)),
                ('MemberOfHousehold', models.CharField(max_length=25)),
                ('tribe_or_nationality', models.CharField(max_length=25)),
                ('religion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Homes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=15)),
                ('hm_code', models.CharField(max_length=8)),
                ('locations', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Homested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hs_code', models.CharField(max_length=7)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='homes',
            name='hs_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainCensus.Homested'),
        ),
        migrations.AddField(
            model_name='general',
            name='hm_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainCensus.Homes'),
        ),
        migrations.AddField(
            model_name='general',
            name='hs_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainCensus.Homested'),
        ),
    ]