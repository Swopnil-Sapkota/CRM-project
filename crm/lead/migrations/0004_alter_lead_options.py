# Generated by Django 5.1.3 on 2024-11-27 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_lead_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lead',
            options={'ordering': ('-created_at',)},
        ),
    ]