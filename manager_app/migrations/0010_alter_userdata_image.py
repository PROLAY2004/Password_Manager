# Generated by Django 5.1.5 on 2025-02-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0009_alter_userdata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
