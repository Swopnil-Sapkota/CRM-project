# Generated by Django 5.1.3 on 2024-11-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('max_leads', models.IntegerField()),
                ('max_clients', models.IntegerField()),
            ],
        ),
    ]