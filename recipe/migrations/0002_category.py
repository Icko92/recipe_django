# Generated by Django 3.1.6 on 2021-02-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('recipes', models.ManyToManyField(to='recipe.Recipe')),
            ],
        ),
    ]
