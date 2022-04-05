# Generated by Django 3.2.12 on 2022-03-31 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LFPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('text', models.CharField(blank=True, default=None, max_length=256)),
                ('pic1', models.FileField(blank=True, upload_to='')),
                ('pic2', models.FileField(blank=True, upload_to='')),
                ('pic3', models.FileField(blank=True, upload_to='')),
                ('public', models.BooleanField()),
                ('time', models.DateTimeField()),
                ('status', models.SmallIntegerField(default=0)),
                ('type', models.CharField(choices=[('L', 'Lost'), ('F', 'Found')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='LFReply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('author', models.CharField(max_length=32)),
                ('text', models.CharField(blank=True, default=None, max_length=256)),
                ('pic1', models.FileField(blank=True, upload_to='')),
                ('pic2', models.FileField(blank=True, upload_to='')),
                ('pic3', models.FileField(blank=True, upload_to='')),
                ('public', models.BooleanField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]