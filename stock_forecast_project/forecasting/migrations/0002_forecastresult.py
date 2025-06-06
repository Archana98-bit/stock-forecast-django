# Generated by Django 5.2.1 on 2025-05-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForecastResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('forecast_date', models.DateField()),
                ('predicted_value', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
