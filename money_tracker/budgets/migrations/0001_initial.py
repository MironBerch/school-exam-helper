# Generated by Django 4.2.4 on 2023-08-30 17:57

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
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.FloatField(default=0, verbose_name='overall budget')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='budget', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'budget',
                'verbose_name_plural': 'budgets',
            },
        ),
    ]
