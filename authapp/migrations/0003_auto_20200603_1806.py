# Generated by Django 3.0.5 on 2020-06-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_fill_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hohoouser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='аккаунт активен'),
        ),
    ]
