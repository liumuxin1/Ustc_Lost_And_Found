# Generated by Django 3.2.12 on 2022-04-01 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lfpost',
            name='title',
            field=models.CharField(default='物品丢失', max_length=64),
        ),
    ]