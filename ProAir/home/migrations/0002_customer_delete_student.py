# Generated by Django 4.0.3 on 2022-08-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]