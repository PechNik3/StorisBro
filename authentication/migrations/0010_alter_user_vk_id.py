# Generated by Django 5.0 on 2024-03-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_user_count_of_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vk_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='VK id'),
        ),
    ]
