# Generated by Django 2.1.3 on 2018-12-06 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20181205_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='username',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]