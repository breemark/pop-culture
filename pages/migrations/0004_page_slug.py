# Generated by Django 3.1.5 on 2021-02-08 14:46

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210208_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='hola', editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]
