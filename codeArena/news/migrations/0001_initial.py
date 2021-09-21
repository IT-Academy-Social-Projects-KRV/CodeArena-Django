# Generated by Django 3.2.5 on 2021-09-06 22:33

import django.core.validators
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70, validators=[django.core.validators.MinLengthValidator(20)])),
                ('content', models.TextField()),
                ('src', models.ImageField(upload_to='news_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]