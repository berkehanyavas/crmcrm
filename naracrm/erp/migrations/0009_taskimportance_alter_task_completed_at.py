# Generated by Django 4.1.6 on 2023-02-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_alter_task_completed_at_alter_team_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskImportance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
