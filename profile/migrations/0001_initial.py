# Generated by Django 4.2.7 on 2023-11-26 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0002_rename_code_country_alpha2_country_alpha3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('national_id', models.CharField(max_length=16)),
                ('passport', models.CharField(max_length=16)),
                ('first_name', models.CharField(max_length=64)),
                ('second_name', models.CharField(max_length=64)),
                ('third_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('U', 'UNSPECIFIED')], max_length=1)),
                ('is_active', models.BooleanField(default=True)),
                ('bio', models.CharField(max_length=1024)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='countries.country')),
            ],
            options={
                'unique_together': {('national_id', 'country'), ('passport', 'country')},
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=32)),
                ('address1', models.CharField(max_length=64)),
                ('address2', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('extra_data', models.JSONField(blank=True, default=dict)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='profile.person')),
            ],
        ),
    ]