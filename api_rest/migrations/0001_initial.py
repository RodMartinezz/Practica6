# Generated by Django 5.0.3 on 2024-03-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cerveza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('sabor', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('presentacion', models.CharField(choices=[('Botella', 'Botella'), ('Lata', 'Lata'), ('Caguama', 'Caguama')], max_length=30)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
