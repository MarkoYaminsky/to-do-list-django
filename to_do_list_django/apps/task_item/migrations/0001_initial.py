# Generated by Django 4.1 on 2022-08-04 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_done', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=20)),
                ('task_value', models.IntegerField()),
            ],
        ),
    ]
