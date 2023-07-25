# Generated by Django 4.2.3 on 2023-07-25 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('period', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'insurance',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('bank_id', models.BigIntegerField(unique=True)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.insurance')),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
