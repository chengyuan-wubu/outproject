# Generated by Django 2.1.2 on 2018-10-18 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sccontent',
            name='contents',
            field=models.TextField(default='null'),
        ),
    ]