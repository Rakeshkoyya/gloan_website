# Generated by Django 3.2.7 on 2021-09-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.TextField(default='----', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='bank_ac',
            field=models.CharField(default='-----', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='ifcs',
            field=models.CharField(default='----', max_length=15),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default='0000', max_length=10),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
