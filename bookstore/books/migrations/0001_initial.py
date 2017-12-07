# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('type_id', models.SmallIntegerField(default=1, choices=[(1, 'python'), (2, 'Javascript'), (3, '数据结构与算法'), (4, '机器学习'), (5, '操作系统'), (6, '数据库')], verbose_name='书籍种类')),
                ('title', models.CharField(max_length=50, verbose_name='书籍名称')),
                ('desc', models.CharField(max_length=50, verbose_name='书籍简介')),
                ('price', models.IntegerField(default=0, verbose_name='书籍价格')),
                ('detail', tinymce.models.HTMLField(verbose_name='书籍详情')),
                ('unit', models.CharField(max_length=5, verbose_name='书籍单位')),
                ('sales', models.IntegerField(default=0, verbose_name='书籍销量')),
                ('image', models.ImageField(upload_to='books', verbose_name='商品图片')),
                ('status', models.SmallIntegerField(default=1, choices=[(0, '下线'), (1, '上线')], verbose_name='商品状态')),
            ],
            options={
                'db_table': 's_book_info',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('hcontent', tinymce.models.HTMLField()),
            ],
        ),
    ]
