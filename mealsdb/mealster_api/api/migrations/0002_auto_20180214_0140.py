# Generated by Django 2.0.2 on 2018-02-14 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit_of_measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.UnitOfMeasure'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='serves',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
