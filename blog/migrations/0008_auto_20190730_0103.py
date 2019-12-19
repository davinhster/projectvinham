# Generated by Django 2.2.2 on 2019-07-30 01:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190730_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]