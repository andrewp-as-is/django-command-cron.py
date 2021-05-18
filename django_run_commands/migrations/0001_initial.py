# Generated by Django 3.1.7 on 2021-05-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('args', models.CharField(blank=True, max_length=255, null=True)),
                ('separator', models.TextField(default=' ')),
                ('seconds', models.IntegerField()),
                ('order', models.IntegerField(default=0)),
                ('is_disabled', models.BooleanField(null=True, verbose_name='disabled')),
                ('is_logged', models.BooleanField(null=True, verbose_name='logged')),
                ('is_running', models.BooleanField(default=False, verbose_name='running')),
                ('started_at', models.DateTimeField(null=True)),
                ('completed_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'run_commands_command',
                'ordering': ('name', 'args'),
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('args', models.CharField(blank=True, max_length=255, null=True)),
                ('separator', models.TextField(null=True)),
                ('out', models.TextField()),
                ('started_at', models.DateTimeField()),
                ('completed_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'run_commands_log',
                'ordering': ('-completed_at',),
            },
        ),
        migrations.AddIndex(
            model_name='log',
            index=models.Index(fields=['name'], name='run_command_name_e0ea15_idx'),
        ),
        migrations.AddIndex(
            model_name='log',
            index=models.Index(fields=['-started_at'], name='run_command_started_49095c_idx'),
        ),
        migrations.AddIndex(
            model_name='log',
            index=models.Index(fields=['-completed_at'], name='run_command_complet_7c879e_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['name'], name='run_command_name_d22ec3_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['is_disabled'], name='run_command_is_disa_6bd433_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['is_running'], name='run_command_is_runn_2ef373_idx'),
        ),
    ]
