# Generated by Django 5.0.6 on 2024-06-23 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product',
        ),
    ]