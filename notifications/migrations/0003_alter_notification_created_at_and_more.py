# Generated by Django 5.1.4 on 2024-12-16 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_alter_notification_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(verbose_name='Mensaje'),
        ),
    ]
