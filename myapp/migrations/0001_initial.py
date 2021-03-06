# Generated by Django 3.1 on 2020-08-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.CharField(max_length=10)),
                ('Temail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=8)),
                ('phonenumber', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
