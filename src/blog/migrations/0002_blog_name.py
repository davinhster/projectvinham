# Generated by Django 2.2.2 on 2019-07-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default=True, max_length=120),
            preserve_default=False,
        ),
    ]
