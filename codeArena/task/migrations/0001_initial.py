# Generated by Django 3.2.5 on 2021-08-30 09:57

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('user_id', models.CharField(max_length=32)),
                ('unit_test', models.FileField(max_length=500, upload_to='')),
                ('rate', models.IntegerField()),
                ('level', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='task.category')),
                ('languages', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='task.language')),
            ],
        ),
        migrations.CreateModel(
            name='CoderTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coder_id', models.CharField(default='', max_length=36)),
                ('solution', models.TextField()),
                ('status', models.BooleanField()),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]
