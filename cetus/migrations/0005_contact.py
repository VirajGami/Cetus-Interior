# Generated by Django 3.1.1 on 2023-02-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cetus', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Number', models.IntegerField()),
                ('Message', models.CharField(max_length=200)),
            ],
        ),
    ]