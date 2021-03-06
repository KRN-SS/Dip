# Generated by Django 3.2.12 on 2022-04-06 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0159_remove_broken_endpoint_statuses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint_status',
            name='endpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_endpoint', to='dojo.endpoint'),
        ),
        migrations.AlterField(
            model_name='endpoint_status',
            name='finding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_finding', to='dojo.finding'),
        ),
    ]
