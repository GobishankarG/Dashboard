# Generated by Django 5.1.3 on 2024-12-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myap', '0005_remove_register_table_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='details_table',
            name='username',
            field=models.CharField(default='default_username', max_length=20),
        ),
    ]