# Generated by Django 3.2.4 on 2021-07-28 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telesettings',
            old_name='th_message',
            new_name='tg_message',
        ),
    ]
