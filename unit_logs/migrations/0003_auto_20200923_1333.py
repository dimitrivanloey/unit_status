# Generated by Django 3.1.1 on 2020-09-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0002_auto_20200923_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='status',
            field=models.CharField(choices=[('STICK', 'Stick'), ('FAILED', 'Failed'), ('MISSING', 'Missing')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='unit',
            name='type',
            field=models.CharField(choices=[('DENMAN', 'Denman'), ('WINX', 'Winx'), ('ARKLE', 'Arkle'), ('FRANKEL', 'Frankel'), ('ENABLE', 'Enable'), ('KAUTO', 'Kauto')], default='WINX', max_length=10),
        ),
    ]
