# Generated by Django 5.1 on 2024-08-30 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aluno', '0008_amigos_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amigos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
