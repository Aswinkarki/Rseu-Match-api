# Generated by Django 5.1.7 on 2025-03-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
