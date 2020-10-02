# Generated by Django 3.1.1 on 2020-09-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0010_auto_20200923_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='status',
            field=models.CharField(choices=[('STICK', 'Stick'), ('FAILED', 'Failed'), ('MISSING', 'Missing')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='unit',
            name='type',
            field=models.CharField(choices=[('A', 'Arkle'), ('D', 'Denman'), ('E', 'Enable'), ('W', 'Winx'), ('F', 'Frankel'), ('K', 'Kauto')], default='W', max_length=10),
        ),
    ]