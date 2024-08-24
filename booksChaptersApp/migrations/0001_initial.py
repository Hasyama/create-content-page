# Generated by Django 5.1 on 2024-08-24 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books_DB',
            fields=[
                ('book_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='chapters_DB',
            fields=[
                ('chapter_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=100)),
                ('book_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booksChaptersApp.books_db')),
            ],
        ),
    ]
