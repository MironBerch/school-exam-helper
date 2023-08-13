# Generated by Django 4.2.2 on 2023-08-13 22:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name of category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='slug for category'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='expense amount')),
                ('name', models.CharField(max_length=50, verbose_name='expense name')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='expense description')),
                ('cost_accounting_date', models.DateField(auto_now_add=True, verbose_name='cost accounting date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='expense modified date')),
                ('expense_date', models.DateField(verbose_name='date of expense')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='expenses.category', verbose_name='expense category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='expense author')),
            ],
            options={
                'verbose_name': 'expense',
                'verbose_name_plural': 'expenses',
                'ordering': ('expense_date',),
            },
        ),
    ]
