# Generated by Django 3.0.7 on 2021-09-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0044_auto_20210921_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='large_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='icon_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='optimised_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
