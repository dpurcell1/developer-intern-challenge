# Generated by Django 3.1.5 on 2021-01-18 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo_app', '0002_auto_20210118_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img',
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
