# Generated by Django 2.0.1 on 2018-02-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iss',
            name='cust',
        ),
        migrations.AddField(
            model_name='iss',
            name='department',
            field=models.CharField(default='unassigned', max_length=1024),
        ),
    ]