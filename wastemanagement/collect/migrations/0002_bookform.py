# Generated by Django 2.2.5 on 2020-05-25 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenno', models.CharField(max_length=100)),
                ('cname', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('wastetype', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
