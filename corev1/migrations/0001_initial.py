<<<<<<< HEAD
# Generated by Django 4.0.3 on 2022-04-03 21:20

import datetime
from django.db import migrations, models
import uuid
=======
# Generated by Django 4.0.3 on 2022-04-02 03:23

from django.db import migrations, models
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='OrganizationModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
=======
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5
                ('password', models.CharField(max_length=30)),
                ('organization', models.CharField(max_length=30)),
            ],
        ),
    ]
