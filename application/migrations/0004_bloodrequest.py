# Generated by Django 3.2.13 on 2022-05-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_camp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodrequest',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('bloodid', models.CharField(max_length=100)),
                ('nounit', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
        ),
    ]
