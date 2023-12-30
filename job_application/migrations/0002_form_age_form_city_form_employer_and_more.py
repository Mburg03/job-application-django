# Generated by Django 5.0 on 2023-12-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='employer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='employment_duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='street_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
