# Generated by Django 5.0 on 2025-01-07 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yangiliklar',
            name='video',
            field=models.URLField(default='app'),
            preserve_default=False,
        ),
    ]
