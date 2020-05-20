# Generated by Django 3.0.5 on 2020-05-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='idcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('employment_id', models.CharField(max_length=20, null=True)),
                ('customer_account_no', models.CharField(max_length=20, null=True)),
                ('circle', models.CharField(max_length=20, null=True)),
                ('company_name', models.CharField(max_length=20, null=True)),
                ('department', models.CharField(max_length=20, null=True)),
                ('certificate_no', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
