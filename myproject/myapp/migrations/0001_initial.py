# Generated by Django 4.1.1 on 2022-10-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
            ],
        ),
    ]
