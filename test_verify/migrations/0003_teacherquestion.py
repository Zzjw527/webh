# Generated by Django 3.1.2 on 2020-11-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_verify', '0002_auto_20201102_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacherquestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=100)),
                ('detail', models.CharField(default='', max_length=100)),
                ('author', models.CharField(default='', max_length=32)),
            ],
        ),
    ]
