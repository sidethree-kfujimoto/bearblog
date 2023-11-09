# Generated by Django 4.0.4 on 2022-07-15 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0053_blog_meta_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='dark_mode',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_tag',
            field=models.CharField(blank=True, help_text='Custom meta tag', max_length=500),
        ),
    ]