# Generated by Django 4.2.4 on 2024-01-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='info-img/'),
        ),
        migrations.AlterField(
            model_name='info',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='title',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
