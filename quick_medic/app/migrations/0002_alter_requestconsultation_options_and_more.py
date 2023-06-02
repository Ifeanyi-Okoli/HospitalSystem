# Generated by Django 4.2.1 on 2023-05-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestconsultation',
            options={'permissions': (('can_consult', 'Consult Doctor'),)},
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='image',
        ),
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]