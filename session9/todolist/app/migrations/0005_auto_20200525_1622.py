# Generated by Django 3.0.6 on 2020-05-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200525_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='duedate',
            field=models.DateField(null=True),
        ),
    ]
