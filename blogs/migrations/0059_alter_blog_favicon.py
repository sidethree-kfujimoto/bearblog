# Generated by Django 4.0.4 on 2022-07-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0058_remove_blog_dark_mode_alter_blog_nav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='favicon',
            field=models.CharField(default='🐼', max_length=10),
        ),
    ]
