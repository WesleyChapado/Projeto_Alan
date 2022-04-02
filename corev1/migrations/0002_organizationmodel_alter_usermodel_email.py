# Generated by Django 4.0.3 on 2022-04-02 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corev1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
                ('created', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]