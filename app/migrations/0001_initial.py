# Generated by Django 3.2.8 on 2022-01-22 16:15

from django.db import migrations, models
import django.forms.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('created', models.DateField(verbose_name=django.forms.fields.DateTimeField)),
            ],
        ),
    ]