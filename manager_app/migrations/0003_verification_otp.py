# Generated by Django 5.1.5 on 2025-02-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0002_alter_userdata_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification_otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=4)),
            ],
        ),
    ]
