# Generated by Django 3.2.16 on 2023-01-09 14:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cash_dividend_record',
            new_name='CashDividendRecord',
        ),
        migrations.RenameModel(
            old_name='stock_info',
            new_name='StockInfo',
        ),
        migrations.RenameModel(
            old_name='trade_record',
            new_name='TradeRecord',
        ),
        migrations.AlterModelTable(
            name='cashdividendrecord',
            table='cash_dividend_record',
        ),
        migrations.AlterModelTable(
            name='company',
            table='company',
        ),
        migrations.AlterModelTable(
            name='stockinfo',
            table='stock_info',
        ),
        migrations.AlterModelTable(
            name='traderecord',
            table='trade_record',
        ),
    ]
