# Generated by Django 2.2.7 on 2019-11-25 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_employee_hotel_main_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='hotel_Main_Img',
        ),
    ]
