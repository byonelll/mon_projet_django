# Generated by Django 5.1.3 on 2024-11-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_member_phone_contribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
