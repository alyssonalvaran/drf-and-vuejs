# Generated by Django 2.2.6 on 2019-10-14 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20191014_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
    ]