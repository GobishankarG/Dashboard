# Generated by Django 5.1.3 on 2024-12-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myap', '0008_details_table_cur_date_details_table_cur_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details_table',
            name='cur_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='details_table',
            name='cur_time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
