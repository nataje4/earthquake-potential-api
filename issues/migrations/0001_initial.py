# Generated by Django 3.0.5 on 2020-04-03 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('website', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateField(verbose_name='date submitted')),
                ('title', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('text', models.TextField()),
                ('media_file', models.FileField(upload_to='issue_media/%Y/%m/')),
                ('layout_type', models.CharField(max_length=20)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Issue')),
            ],
        ),
    ]