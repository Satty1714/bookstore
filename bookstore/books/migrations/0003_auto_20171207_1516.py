# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20171205_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='details',
        ),
        migrations.AddField(
            model_name='books',
            name='stock',
            field=models.IntegerField(default=1, verbose_name='商品库存'),
        ),
        migrations.AlterField(
            model_name='books',
            name='desc',
            field=models.CharField(max_length=128, verbose_name='商品简介'),
        ),
        migrations.AlterField(
            model_name='books',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name='商品详情'),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='books',
            name='sales',
            field=models.IntegerField(default=0, verbose_name='商品销量'),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=20, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(default=1, choices=[(1, 'python'), (2, 'Javascript'), (3, '数据结构与算法'), (4, '机器学习'), (5, '操作系统'), (6, '数据库')], verbose_name='商品种类'),
        ),
        migrations.AlterField(
            model_name='books',
            name='unit',
            field=models.CharField(max_length=20, verbose_name='商品单位'),
        ),
        migrations.AlterModelTable(
            name='books',
            table='s_books',
        ),
    ]
