# Generated by Django 2.1.7 on 2020-05-14 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('description', models.TextField()),
                ('labels', models.CharField(choices=[('Per', 'Personal'), ('Wor', 'Work'), ('Sho', 'Shopping'), ('Oth', 'Others')], max_length=3)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('act', 'Active'), ('don', 'Done')], max_length=3)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
