# Generated by Django 4.2.6 on 2023-10-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_admission_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='admission_no',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]