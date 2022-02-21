# Generated by Django 3.2 on 2022-02-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockInfoScraper', '0010_auto_20220221_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='stock_memo',
            name='main_goods_or_services',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='stock_memo',
            name='my_note',
            field=models.CharField(max_length=2048),
        ),
    ]
