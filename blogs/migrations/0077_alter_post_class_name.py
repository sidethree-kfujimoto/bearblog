# Generated by Django 4.0.4 on 2022-09-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0076_post_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='class_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
