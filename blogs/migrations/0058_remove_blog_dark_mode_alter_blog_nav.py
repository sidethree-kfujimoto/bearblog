# Generated by Django 4.0.4 on 2022-07-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0057_alter_blog_meta_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='dark_mode',
        ),
        migrations.AlterField(
            model_name='blog',
            name='nav',
            field=models.CharField(blank=True, default='[Home](/)[Blog](/blog/)', max_length=500),
        ),
    ]
