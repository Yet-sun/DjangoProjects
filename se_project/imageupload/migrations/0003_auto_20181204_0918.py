# Generated by Django 2.1.3 on 2018-12-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0002_auto_20181204_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_directory_path'),
        ),
    ]
