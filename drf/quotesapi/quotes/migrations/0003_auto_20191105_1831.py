# Generated by Django 2.2.6 on 2019-11-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20191105_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='context',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
