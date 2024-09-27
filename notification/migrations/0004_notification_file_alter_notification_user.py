from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0003_alter_notification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files', verbose_name='Файл для креатива'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL, to_field='UID'),
        ),
    ]
