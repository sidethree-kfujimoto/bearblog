# Generated by Django 4.0.4 on 2022-08-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0069_blog_last_modified_post_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_template',
            field=models.TextField(blank=True),
        ),
    ]
