# Generated by Django 3.0.8 on 2020-08-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default='2020-08-27 09:14:24'),
        ),
    ]
