# Generated by Django 3.2.6 on 2021-08-24 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title_tab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title_tab',
            new_name='title_tag',
        ),
    ]