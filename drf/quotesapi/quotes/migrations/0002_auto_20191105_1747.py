# Generated by Django 2.2.6 on 2019-11-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='context',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
