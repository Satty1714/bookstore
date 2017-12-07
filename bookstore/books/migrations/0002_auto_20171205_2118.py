# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeroInfo',
        ),
        migrations.AddField(
            model_name='books',
            name='details',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AlterField(
            model_name='books',
            name='detail',
            field=models.CharField(verbose_name='书籍详情', max_length=500),
        ),
    ]
