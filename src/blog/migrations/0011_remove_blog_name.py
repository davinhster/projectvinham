# Generated by Django 2.2.2 on 2019-07-30 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190730_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
    ]
