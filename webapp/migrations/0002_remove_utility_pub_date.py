# Generated by Django 2.0.2 on 2018-02-02 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utility',
            name='pub_date',
        ),
    ]