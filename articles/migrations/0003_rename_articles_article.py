# Generated by Django 5.1 on 2024-10-13 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_add_date_articles_adate_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
    ]
