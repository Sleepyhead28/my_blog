# Generated by Django 2.1 on 2018-08-23 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0002_entry_1'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry_1',
            options={'verbose_name_plural': 'entries1'},
        ),
        migrations.AlterModelOptions(
            name='topic_1',
            options={'verbose_name_plural': 'topics1'},
        ),
    ]
