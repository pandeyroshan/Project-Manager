# Generated by Django 2.1.5 on 2019-08-01 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20190801_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
