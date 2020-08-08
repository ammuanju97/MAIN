# Generated by Django 2.2.5 on 2020-05-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0003_auto_20200525_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.BigIntegerField()),
                ('expirydate', models.DateField()),
                ('cvv', models.IntegerField()),
                ('nameofcard', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SellPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.BigIntegerField()),
                ('expirydate', models.DateField()),
                ('cvv', models.IntegerField()),
                ('nameofcard', models.CharField(max_length=100)),
            ],
        ),
    ]