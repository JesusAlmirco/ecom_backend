# Generated by Django 4.0.5 on 2022-06-10 15:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('not_processed', 'Not Processed'), ('processed', 'Processed'), ('shipped', 'Shipping'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='not_processed', max_length=50)),
                ('transaction_id', models.CharField(max_length=255, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('full_name', models.CharField(max_length=255)),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state_province_region', models.CharField(max_length=255)),
                ('postal_zip_code', models.CharField(max_length=20)),
                ('country_region', models.CharField(choices=[('Peru', 'Peru')], default='Peru', max_length=255)),
                ('telephone_number', models.CharField(max_length=255)),
                ('shipping_name', models.CharField(max_length=255)),
                ('shipping_time', models.CharField(max_length=255)),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_issued', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('count', models.IntegerField()),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
    ]
