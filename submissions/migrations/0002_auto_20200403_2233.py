# Generated by Django 3.0.5 on 2020-04-03 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='editor_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
