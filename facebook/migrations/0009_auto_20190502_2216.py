# Generated by Django 2.2 on 2019-05-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0008_auto_20190502_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
