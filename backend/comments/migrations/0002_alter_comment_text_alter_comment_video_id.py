# Generated by Django 4.1.7 on 2023-02-15 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video_id',
            field=models.CharField(max_length=30),
        ),
    ]