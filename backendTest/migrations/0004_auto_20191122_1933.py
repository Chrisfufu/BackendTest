# Generated by Django 2.2.7 on 2019-11-23 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendTest', '0003_auto_20191122_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='profile',
            field=models.ForeignKey(db_column='profile', on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='backendTest.Profile'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='actions',
            field=models.ForeignKey(db_column='actions', on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='backendTest.Actions'),
        ),
    ]
