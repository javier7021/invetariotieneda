# Generated by Django 3.1.7 on 2021-04-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20210421_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='fecha_de_expliracion',
            new_name='fecha_de_Vencimiento',
        ),
        migrations.AlterField(
            model_name='kardex',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='provedores',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
