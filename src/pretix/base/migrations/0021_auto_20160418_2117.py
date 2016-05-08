# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 21:17
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0020_auto_20160418_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='item',
            field=models.ForeignKey(blank=True, help_text="This product is added to the user's cart if the voucher is redeemed.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vouchers', to='pretixbase.Item', verbose_name='Product'),
        ),
    ]