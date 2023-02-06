# Generated by Django 4.1.6 on 2023-02-05 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_followerscount_alter_post_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followerscount',
            old_name='followers',
            new_name='follower',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 5, 21, 52, 17, 63578)),
        ),
    ]