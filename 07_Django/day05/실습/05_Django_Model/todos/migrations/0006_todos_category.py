# Generated by Django 3.2.18 on 2023-03-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_remove_todos_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='category',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
