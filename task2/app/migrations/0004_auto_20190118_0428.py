# Generated by Django 2.1.5 on 2019-01-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_estimate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
