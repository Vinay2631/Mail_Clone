# Generated by Django 4.0.4 on 2022-04-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmail', '0004_alter_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.CharField(error_messages={'unique': 'Email Already Exists'}, max_length=100),
        ),
    ]