# Generated by Django 5.0 on 2023-12-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0003_alter_form_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]