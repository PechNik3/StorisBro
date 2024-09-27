# Generated by Django 5.0 on 2024-02-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0008_alter_statuscommunities_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitymodel',
            name='name_id_commission',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='ID сообщества'),
        ),
        migrations.AddField(
            model_name='communitymodel',
            name='status_commission',
            field=models.BooleanField(default=False, verbose_name='Статус ссылки'),
        ),
        migrations.AddField(
            model_name='communitymodel',
            name='url_commission',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка которая должна быть в сообществе'),
        ),
    ]
