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
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('count', models.IntegerField(default=1, verbose_name='商品数量')),
                ('price', models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')),
                ('books', models.ForeignKey(to='books.Books', verbose_name='订单商品')),
            ],
            options={
                'db_table': 's_order_books',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order_id', models.CharField(primary_key=True, max_length=64, verbose_name='订单编号', serialize=False)),
                ('total_count', models.IntegerField(default=1, verbose_name='商品总数')),
                ('total_price', models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总价')),
                ('transit_price', models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单运费')),
                ('pay_method', models.SmallIntegerField(choices=[(1, '货到付款'), (2, '微信支付'), (3, '支付宝'), (4, '银联支付')], default=1, verbose_name='支付方式')),
                ('status', models.SmallIntegerField(choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')], default=1, verbose_name='订单状态')),
                ('trade_id', models.CharField(max_length=100, null=True, blank=True, verbose_name='支付编号', unique=True)),
                ('addr', models.ForeignKey(to='users.Address', verbose_name='收货地址')),
                ('passport', models.ForeignKey(to='users.User', verbose_name='下单账户')),
            ],
            options={
                'db_table': 's_order_info',
            },
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(to='order.OrderInfo', verbose_name='所属订单'),
        ),
    ]
