# Generated by Django 3.1.2 on 2020-11-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False, verbose_name='userId')),
                ('userName', models.CharField(max_length=50, verbose_name='userName')),
                ('userNickName', models.CharField(max_length=50, verbose_name='userNickName')),
                ('userPassWord', models.CharField(max_length=50, verbose_name='userPassWord')),
                ('userEmail', models.CharField(max_length=50, verbose_name='userEmail')),
                ('userPhone', models.CharField(max_length=50, verbose_name='userPhone')),
                ('isAdmin', models.SmallIntegerField(verbose_name='isAdmin')),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'unique_together': {('userId', 'userName')},
            },
        ),
    ]
