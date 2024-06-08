# Generated by Django 3.2.9 on 2024-06-06 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opencontractserver.shared.defaults
import opencontractserver.shared.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extracts', '0006_auto_20240602_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacell',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_cells', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='datacell',
            name='corrected_data',
            field=opencontractserver.shared.fields.NullableJSONField(blank=True, default=opencontractserver.shared.defaults.jsonfield_default_value, null=True),
        ),
        migrations.AddField(
            model_name='datacell',
            name='rejected_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rejected_cells', to=settings.AUTH_USER_MODEL),
        ),
    ]
