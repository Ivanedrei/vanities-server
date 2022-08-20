# Generated by Django 4.1 on 2022-08-20 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='VanityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vanities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vanitiesapi.color')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vanitiesapi.size')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vanitiesapi.vanitytype')),
                ('wood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vanitiesapi.wood')),
            ],
        ),
    ]