# Generated by Django 2.2.5 on 2020-03-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200325_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_secret',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email_verified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='login_method',
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('krw', 'USD'), ('krw', 'KRW')], max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('kr', 'Korean')], max_length=2),
        ),
    ]
