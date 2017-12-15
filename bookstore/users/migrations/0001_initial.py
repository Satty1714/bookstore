# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('recipient_name', models.CharField(max_length=20, verbose_name='收件人')),
                ('recipient_addr', models.CharField(max_length=222, verbose_name='收件人地址')),
                ('zip_code', models.CharField(max_length=6, verbose_name='邮政编码')),
                ('recipient_phone', models.CharField(max_length=11, verbose_name='电话')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
            ],
            options={
                'db_table': 's_user_address',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=20, verbose_name='用户名称')),
                ('password', models.CharField(max_length=40, verbose_name='用户密码')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('is_active', models.BooleanField(default=False, verbose_name='激活状态')),
            ],
            options={
                'db_table': 's_user_account',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='passport',
            field=models.ForeignKey(to='users.User'),
        ),
    ]
