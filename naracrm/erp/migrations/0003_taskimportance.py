# Generated by Django 4.1.7 on 2023-02-21 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_rename_description_task_aciklama_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskImportance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='importance', to='erp.task')),
            ],
        ),
    ]
