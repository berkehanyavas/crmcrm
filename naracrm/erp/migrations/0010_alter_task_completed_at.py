# Generated by Django 4.1.6 on 2023-02-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0009_taskimportance_alter_task_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]