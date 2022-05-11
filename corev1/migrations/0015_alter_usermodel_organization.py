# Generated by Django 4.0.3 on 2022-04-15 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corev1', '0014_alter_usermodel_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='corev1.organizationmodel'),
        ),
    ]
