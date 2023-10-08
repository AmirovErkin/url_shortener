# Generated by Django 4.1.3 on 2023-10-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('shortened_url', models.CharField(max_length=10, unique=True)),
                ('click_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
