# Generated by Django 2.2.17 on 2020-11-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='session_token',
            field=models.CharField(default=0, max_length=50),
        ),
    ]