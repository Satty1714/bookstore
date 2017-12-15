# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('show', models.BooleanField(default=True, verbose_name='显示评论')),
                ('content', models.CharField(max_length=1000, verbose_name='评论内容')),
                ('book', models.ForeignKey(verbose_name='书籍id', to='books.Books')),
                ('user', models.ForeignKey(default='', verbose_name='用户id', to='users.User')),
            ],
            options={
                'db_table': 's_comments',
            },
        ),
    ]
