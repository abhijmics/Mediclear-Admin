# Generated by Django 3.0.5 on 2020-05-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200513_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('gender', models.CharField(max_length=120, null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('dob', models.CharField(max_length=120, null=True)),
                ('email', models.CharField(max_length=120, null=True)),
                ('q1', models.CharField(max_length=120, null=True)),
                ('q2', models.CharField(max_length=120, null=True)),
                ('q3', models.CharField(max_length=120, null=True)),
                ('q4', models.CharField(max_length=120, null=True)),
                ('q5', models.CharField(max_length=120, null=True)),
                ('q6', models.CharField(max_length=120, null=True)),
                ('q7', models.CharField(max_length=120, null=True)),
                ('q8', models.CharField(max_length=120, null=True)),
                ('q9', models.CharField(max_length=120, null=True)),
                ('q10', models.CharField(max_length=120, null=True)),
                ('q11', models.CharField(max_length=120, null=True)),
                ('comment', models.CharField(max_length=120, null=True)),
                ('height', models.CharField(max_length=120, null=True)),
                ('weight', models.CharField(max_length=120, null=True)),
                ('systolic', models.CharField(max_length=120, null=True)),
                ('diastolic', models.CharField(max_length=120, null=True)),
                ('pulserate', models.CharField(max_length=120, null=True)),
                ('heartsound', models.CharField(max_length=120, null=True)),
                ('peripheralpulse', models.CharField(max_length=120, null=True)),
                ('chestlung', models.CharField(max_length=120, null=True)),
                ('curvicalspine', models.CharField(max_length=120, null=True)),
                ('backmovements', models.CharField(max_length=120, null=True)),
                ('upperlimbs', models.CharField(max_length=120, null=True)),
                ('jointmovements', models.CharField(max_length=120, null=True)),
                ('reflexes', models.CharField(max_length=120, null=True)),
                ('rombergs', models.CharField(max_length=120, null=True)),
                ('hearing', models.CharField(max_length=120, null=True)),
                ('vision', models.CharField(max_length=120, null=True)),
                ('albumin', models.CharField(max_length=120, null=True)),
                ('sugar', models.CharField(max_length=120, null=True)),
                ('blood_group', models.CharField(max_length=120, null=True)),
                ('rh_factor', models.CharField(max_length=120, null=True)),
                ('hb', models.CharField(max_length=120, null=True)),
                ('tlc', models.CharField(max_length=120, null=True)),
                ('rbc', models.CharField(max_length=120, null=True)),
                ('plateletscount', models.CharField(max_length=120, null=True)),
                ('triglycerides', models.CharField(max_length=120, null=True)),
                ('hdl', models.CharField(max_length=120, null=True)),
                ('ldl', models.CharField(max_length=120, null=True)),
                ('result', models.CharField(max_length=120, null=True)),
                ('registration_no', models.CharField(max_length=120, null=True)),
                ('date_of_examination', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
