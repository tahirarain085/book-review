# Generated by Django 4.2.19 on 2025-02-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_isbn_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
