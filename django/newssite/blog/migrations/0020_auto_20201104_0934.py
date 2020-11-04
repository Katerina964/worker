# Generated by Django 3.0.8 on 2020-11-04 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_auto_20201102_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='user',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.CharField(blank=True, max_length=20, verbose_name='Заработная плата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.CharField(blank=True, max_length=20, verbose_name='Заработная плата'),
        ),
    ]
