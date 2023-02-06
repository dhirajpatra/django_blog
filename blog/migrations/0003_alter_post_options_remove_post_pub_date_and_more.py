# Generated by Django 4.0.4 on 2023-02-06 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='post',
            name='date published',
            field=models.DateField(default=datetime.date(2023, 2, 6), verbose_name='pub_date'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=1000, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
    ]