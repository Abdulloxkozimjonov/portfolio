# Generated by Django 4.2.4 on 2024-01-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_info_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='info',
            name='text',
        ),
        migrations.RemoveField(
            model_name='info',
            name='title',
        ),
    ]
