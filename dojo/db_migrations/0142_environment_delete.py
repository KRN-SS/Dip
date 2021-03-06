# Generated by Django 3.2.9 on 2021-12-12 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0141_enable_user_profile_editable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cred_user',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dojo.development_environment'),
        ),
        migrations.AlterField(
            model_name='test',
            name='environment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='dojo.development_environment'),
        ),
    ]
