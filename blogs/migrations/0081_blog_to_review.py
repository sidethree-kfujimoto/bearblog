# Generated by Django 3.1.14 on 2023-04-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0080_auto_20230301_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='to_review',
            field=models.BooleanField(default=False),
        ),
    ]
