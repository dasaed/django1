# Generated by Django 2.0.7 on 2019-05-31 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogreporting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reporter',
            field=models.TextField(default='Oil & Gas Employee'),
        ),
    ]
