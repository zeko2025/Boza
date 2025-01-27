# Generated by Django 5.1 on 2024-10-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('depart', models.CharField(max_length=30)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('upp_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
