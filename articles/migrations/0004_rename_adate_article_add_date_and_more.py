# Generated by Django 5.1 on 2024-10-13 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_articles_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='adate',
            new_name='add_date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='udate',
            new_name='upp_date',
        ),
    ]