# Generated by Django 2.1.3 on 2018-12-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0005_auto_20181214_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=10),
        ),
    ]