# Generated by Django 3.1.7 on 2021-03-31 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0008_auto_20210321_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='lap',
            name='num_cars',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='session_length',
            field=models.IntegerField(default=1500000),
            preserve_default=False,
        ),
    ]
