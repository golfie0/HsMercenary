# Generated by Django 4.0 on 2021-12-20 15:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название карты')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=32, unique=True, verbose_name='UserName')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('register_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=600)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50, verbose_name='Название колоды')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
                ('cards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.card')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField(max_length=600)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
