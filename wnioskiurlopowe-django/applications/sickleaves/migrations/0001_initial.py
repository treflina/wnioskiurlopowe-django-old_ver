# Generated by Django 3.2.9 on 2021-11-09 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sickleave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('C', 'Chorobowe'), ('O', 'Opieka'), ('K', 'Kwarantanna'), ('I', 'Izolacja')], default='C', max_length=10, verbose_name='Rodzaj')),
                ('issue_date', models.DateField(blank=True, null=True, verbose_name='Data wystawienia')),
                ('doc_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nr dokumentu')),
                ('start_date', models.DateField(null=True, verbose_name='Od')),
                ('end_date', models.DateField(null=True, verbose_name='Do')),
                ('additional_info', models.CharField(blank=True, max_length=50, verbose_name='Dodatkowe informacje')),
                ('employee', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sickemployee', to=settings.AUTH_USER_MODEL, verbose_name='osoba')),
            ],
            options={
                'verbose_name': 'Zwolnienie lekarskie',
                'verbose_name_plural': 'Zwolnienia lekarskie',
                'ordering': ['issue_date'],
            },
        ),
    ]