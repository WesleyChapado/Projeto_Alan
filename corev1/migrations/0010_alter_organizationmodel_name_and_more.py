# Generated by Django 4.0.3 on 2022-04-15 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corev1', '0009_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationmodel',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='organizationmodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corev1.organizationmodel'),
        ),
    ]
