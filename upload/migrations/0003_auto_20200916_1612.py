# Generated by Django 3.1.1 on 2020-09-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20200908_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediafile',
            old_name='photo',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='mediafile',
            old_name='title',
            new_name='unique_id',
        ),
        migrations.AddField(
            model_name='mediafile',
            name='questions',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='summary',
            field=models.TextField(default=''),
        ),
    ]
