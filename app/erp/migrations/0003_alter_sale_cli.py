# Generated by Django 3.2.5 on 2022-03-11 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='cli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.client'),
        ),
    ]