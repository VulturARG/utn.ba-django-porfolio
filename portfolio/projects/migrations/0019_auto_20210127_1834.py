# Generated by Django 2.2 on 2021-01-27 21:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20210127_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Descripción'),
        ),
    ]
