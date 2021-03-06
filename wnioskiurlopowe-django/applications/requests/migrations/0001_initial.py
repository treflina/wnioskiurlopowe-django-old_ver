# Generated by Django 3.2.9 on 2021-11-09 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[('W', 'Urlop wypoczynkowy (W)'), ('WS', 'Wolne za pracującą sobotę (WS)'), ('WN', 'Wolne za pracę w niedzielę/święto (WN)'), ('DW', 'Wolne za święto przypadające w wolną sobotę (DW)')], default='', max_length=30, verbose_name='Rodzaj')),
                ('work_date', models.DateField(blank=True, null=True, verbose_name='Data pracującej sob./nd/św.')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Od')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Do')),
                ('days', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ilość dni urlopu')),
                ('status', models.CharField(default='oczekujący', max_length=20)),
                ('substitute', models.CharField(blank=True, max_length=50)),
                ('signed_by', models.CharField(blank=True, max_length=50)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='request_user', to=settings.AUTH_USER_MODEL)),
                ('send_to_person', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wnioski',
                'verbose_name_plural': 'Wnioski',
                'ordering': ['-created'],
            },
        ),
    ]
