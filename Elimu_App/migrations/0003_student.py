# Generated by Django 5.0.2 on 2024-11-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elimu_App', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='student_images/')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
            ],
        ),
    ]