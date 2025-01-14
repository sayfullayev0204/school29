# Generated by Django 5.0 on 2025-01-06 12:10

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yangiliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Asosiy rasm')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Sana')),
            ],
            options={
                'verbose_name': 'Yangiliklar',
                'verbose_name_plural': 'Yangiliklar',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name="Qo'shimcha rasm")),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.yangiliklar', verbose_name='Yangilik')),
            ],
            options={
                'verbose_name': 'Rasmlar',
                'verbose_name_plural': 'Rasmlar',
            },
        ),
        migrations.CreateModel(
            name='YangiliklarTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('sarlavha', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('matn', models.TextField(verbose_name='Matn')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='app.yangiliklar')),
            ],
            options={
                'verbose_name': 'Yangiliklar Translation',
                'db_table': 'app_yangiliklar_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
