# Generated by Django 4.1.6 on 2023-02-07 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('permalink', models.CharField(blank=True, max_length=60, null=True, unique=True)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('bodytext', models.TextField(blank=True, null=True, verbose_name='Page Content')),
            ],
        ),
    ]
