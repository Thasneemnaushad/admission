# Generated by Django 3.0 on 2020-01-13 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=10, null=True)),
                ('subject', models.CharField(blank=True, max_length=30, null=True)),
                ('faculty', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
