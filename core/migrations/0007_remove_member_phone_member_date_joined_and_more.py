from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_joboffer_application'),  # Remplace par la dernière migration précédente.
    ]

    operations = [
        # Ajoute ici les modifications nécessaires à ta base de données.
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone_number',
        ),
    ]
