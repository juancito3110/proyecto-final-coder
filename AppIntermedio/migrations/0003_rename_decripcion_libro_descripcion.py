# Generated by Django 4.0.5 on 2022-07-15 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppIntermedio', '0002_rename_decription_libro_decripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='decripcion',
            new_name='descripcion',
        ),
    ]