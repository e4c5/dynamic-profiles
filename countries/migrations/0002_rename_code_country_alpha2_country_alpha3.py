# Generated by Django 5.0b1 on 2023-10-30 02:54
from django.db import migrations, models
from django.db import connection
from django.conf import settings
import os
from io import StringIO

def load_country_codes(apps, schema_editor):
    with connection.cursor() as cursor:
        csv_file_path = os.path.join(settings.BASE_DIR, 'countries','migrations','all.csv')

        with open(csv_file_path, mode='r') as file:
            data = file.read()
            csv_data = StringIO(data)
        
            cursor.copy_from(csv_data, 'countries_country', 
                             columns=('country', 'alpha2', 'alpha3'), sep='\t')

class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='code',
            new_name='alpha2',
        ),
        migrations.AddField(
            model_name='country',
            name='alpha3',
            field=models.CharField(default=0, max_length=3, unique=True),
            preserve_default=False,
        ),
        migrations.RunPython(load_country_codes)
    ]
