# Generated by Django 3.2.16 on 2023-01-09 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='trade_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plan_type', models.CharField(max_length=32)),
                ('target_price', models.FloatField()),
                ('target_quantity', models.BigIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.company')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_plans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='stock_memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.TextField(default='')),
                ('strategy', models.TextField(default='')),
                ('note', models.TextField(default='')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='stock.company')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_memos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
