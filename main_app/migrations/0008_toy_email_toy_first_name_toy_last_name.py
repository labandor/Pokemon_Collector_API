# Generated by Django 5.0.3 on 2024-04-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_feeding_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='email',
            field=models.CharField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toy',
            name='first_name',
            field=models.CharField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toy',
            name='last_name',
            field=models.CharField(default='null'),
            preserve_default=False,
        ),
    ]