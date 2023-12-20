# Generated by Django 4.2.7 on 2023-12-20 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value1', models.IntegerField()),
                ('value2', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='moisture',
            name='day',
        ),
        migrations.AddField(
            model_name='moisture',
            name='date',
            field=models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, to='core.day'),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='moisture',
            name='time',
            field=models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, to='core.timeline'),
            preserve_default=1,
        ),
    ]