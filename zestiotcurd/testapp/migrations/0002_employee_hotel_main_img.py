# Generated by Django 2.2.7 on 2019-11-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hotel_Main_Img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
