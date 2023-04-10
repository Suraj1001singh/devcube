# Generated by Django 4.1.7 on 2023-04-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.AddField(
            model_name='room',
            name='topic',
            field=models.ManyToManyField(to='base.topic'),
        ),
    ]
