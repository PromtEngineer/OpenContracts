# Generated by Django 3.2.9 on 2022-10-15 21:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import opencontractserver.corpuses.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=1024)),
                ('description', models.TextField(blank=True, default='')),
                ('icon', models.FileField(blank=True, null=True, upload_to=opencontractserver.corpuses.models.calculate_icon_filepath)),
                ('is_public', models.BooleanField(default=False)),
                ('backend_lock', models.BooleanField(default=False)),
                ('error', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('created',),
                'permissions': (('permission_corpus', 'permission corpus'), ('publish_corpus', 'publish corpus'), ('create_corpus', 'create corpus'), ('read_corpus', 'read corpus'), ('update_corpus', 'update corpus'), ('remove_corpus', 'delete corpus')),
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='CorpusGroupObjectPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemporaryFileHandle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=opencontractserver.corpuses.models.calculate_temporary_filepath)),
            ],
        ),
        migrations.CreateModel(
            name='CorpusUserObjectPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpuses.corpus')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
