# Generated by Django 5.0 on 2025-01-07 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_yangiliklar_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yangiliklar',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
