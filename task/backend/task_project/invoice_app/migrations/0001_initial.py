# Generated by Django 4.1.7 on 2023-03-03 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=20)),
                ('total_cost', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_quantity', models.FloatField()),
                ('product_price', models.FloatField()),
                ('product_total_cost', models.FloatField(blank=True, default=0.0, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='invoice_app.invoice')),
            ],
        ),
    ]
