# Generated by Django 2.2.4 on 2020-05-31 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200516_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(height_field=300, null=True, upload_to='profiles', width_field=225),
        ),
    ]