# Generated by Django 3.1.8 on 2021-04-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
