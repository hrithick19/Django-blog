# Generated by Django 3.0.6 on 2020-05-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200521_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='profilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='Pictures/kavidhai')),
            ],
        ),
    ]