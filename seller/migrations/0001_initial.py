# Generated by Django 2.2.12 on 2022-02-15 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120, verbose_name='Product Name')),
                ('brand', models.CharField(blank=True, max_length=120, verbose_name='Brand Name')),
                ('price', models.PositiveIntegerField(default=0)),
                ('details', models.CharField(max_length=1000, verbose_name='Details of Product')),
                ('image', models.ImageField(upload_to='product_images')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='admins.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('stock_available', models.PositiveIntegerField(default=0, help_text='No: of Product Available')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productstock', to='seller.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockadder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
