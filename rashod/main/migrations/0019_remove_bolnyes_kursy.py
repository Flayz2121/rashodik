# Generated by Django 5.1.3 on 2025-02-06 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_bolnyes_kursy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bolnyes',
            name='Kursy',
        ),
    ]
