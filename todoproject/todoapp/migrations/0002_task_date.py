# Generated by Django 3.2.15 on 2022-10-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1989-04-28'),
            preserve_default=False,
        ),
    ]
