# Generated by Django 4.2.6 on 2023-10-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='name of project')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
            ],
        ),
    ]
