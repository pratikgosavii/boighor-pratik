# Generated by Django 3.0.2 on 2020-07-18 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200718_1923'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0005_cart_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='bestseller',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='book_index_1',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='book_index_2',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='book_index_3',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='book_index_4',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='bookback_cover',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='bookfront_cover',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='hot',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='price_new',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='price_old',
        ),
        migrations.AddField(
            model_name='cart',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='home.books'),
        ),
    ]
