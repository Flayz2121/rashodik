# Generated by Django 5.1.3 on 2025-01-27 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='naryads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_of_naryads', models.CharField(max_length=255)),
                ('Kursy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kursy')),
            ],
        ),
    ]
