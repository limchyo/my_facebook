# Generated by Django 2.2 on 2019-05-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0004_auto_20190502_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='password',
            field=models.CharField(max_length=120),
        ),
    ]
