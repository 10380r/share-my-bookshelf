# Generated by Django 3.0.5 on 2020-04-28 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('isbn', models.CharField(max_length=13)),
                ('review', models.TextField(default=0, max_length=1000)),
                ('rabel', models.CharField(default=None, max_length=15)),
                ('star', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_username', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('myself', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_myself', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
