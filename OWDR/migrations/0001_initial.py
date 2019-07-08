# Generated by Django 2.2.2 on 2019-07-08 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourierInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PickUpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=64)),
                ('postal_code', models.CharField(max_length=6)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.ManyToManyField(to='OWDR.ItemDescription')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
                ('mission_description', models.TextField(max_length=1024)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OWDR.Province')),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('picked_up', models.BooleanField(default=False)),
                ('picked_up_date', models.DateField()),
                ('courier_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OWDR.CourierInformation')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OWDR.Institution')),
                ('items', models.ManyToManyField(to='OWDR.ItemType')),
                ('pick_up_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OWDR.PickUpAddress')),
            ],
        ),
    ]
