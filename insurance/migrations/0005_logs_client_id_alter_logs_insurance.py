# Generated by Django 4.2.3 on 2023-08-30 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='client_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='insurance.client'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='insurance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='insurance.insurance'),
        ),
    ]