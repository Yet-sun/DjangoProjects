# Generated by Django 2.1.3 on 2018-12-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='./upload'),
        ),
    ]
