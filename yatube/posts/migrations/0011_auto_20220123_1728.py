# Generated by Django 2.2.16 on 2022-01-23 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20220123_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий'},
        ),
    ]
