# Generated by Django 5.0.7 on 2024-07-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='IdPais',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
