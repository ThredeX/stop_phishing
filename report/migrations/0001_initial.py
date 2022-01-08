# Generated by Django 4.0.1 on 2022-01-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhishingUrl',
            fields=[
                ('domain', models.URLField(primary_key=True, serialize=False, verbose_name='phising url')),
                ('is_verified', models.BooleanField(default=False, verbose_name='is really phishing')),
            ],
        ),
    ]
