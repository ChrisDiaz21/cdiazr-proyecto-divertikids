# Generated by Django 5.1.4 on 2024-12-16 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'Notificación', 'verbose_name_plural': 'Notificaciones'},
        ),
    ]