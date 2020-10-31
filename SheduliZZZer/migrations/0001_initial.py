# Generated by Django 3.1.2 on 2020-10-31 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('abbriviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('course', models.ManyToManyField(related_name='groups', to='SheduliZZZer.Course')),
            ],
        ),
        migrations.CreateModel(
            name='WebConference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('course', models.ManyToManyField(related_name='webConference', to='SheduliZZZer.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('abbriviation', models.CharField(max_length=10)),
                ('course', models.ManyToManyField(related_name='profession', to='SheduliZZZer.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.ManyToManyField(related_name='members', to='SheduliZZZer.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(related_name='experts', to='SheduliZZZer.Course')),
                ('person', models.ManyToManyField(related_name='expert', to='SheduliZZZer.Person')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SheduliZZZer.direction'),
        ),
        migrations.CreateModel(
            name='Coordinater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(related_name='coordinaters', to='SheduliZZZer.Course')),
                ('person', models.ManyToManyField(related_name='coordinater', to='SheduliZZZer.Person')),
            ],
        ),
    ]
