# Generated by Django 3.0.5 on 2020-04-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_auto_20200413_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/avatars/avatar.jpeg', upload_to='images/avatars'),
        ),
    ]
