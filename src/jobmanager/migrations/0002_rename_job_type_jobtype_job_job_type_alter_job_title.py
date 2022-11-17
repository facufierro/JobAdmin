# Generated by Django 4.1.3 on 2022-11-14 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobmanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job_Type',
            new_name='JobType',
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='jobmanager.jobtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
