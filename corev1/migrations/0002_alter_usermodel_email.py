# Generated by Django 4.0.3 on 2022-04-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corev1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
