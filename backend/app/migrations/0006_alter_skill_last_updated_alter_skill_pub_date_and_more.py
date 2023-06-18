# Generated by Django 4.2.2 on 2023-06-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_skill_last_updated_alter_skill_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='last_updated',
            field=models.DateTimeField(verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]