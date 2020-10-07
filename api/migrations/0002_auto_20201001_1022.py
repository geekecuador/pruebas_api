# Generated by Django 3.1.1 on 2020-10-01 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='actividad',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='actividad_en',
            field=models.TextField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='actividad_es',
            field=models.TextField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='hora_fin',
            field=models.TimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.lugar'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='codigo',
            field=models.CharField(blank=True, editable=False, max_length=10, null=True),
        ),
    ]
