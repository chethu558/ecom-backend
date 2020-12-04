from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, shcema_editor):
        user = CustomUser(name="Chethan",
                         email="kmrchethan558@gmail.com",
                         is_staff=True,
                         is_superuser=True,
                         phone="7975506729")
        
        user.set_password("12345678")
        user.save()

    dependencies = []

    operations = [
         migrations.RunPython(seed_data),
     ]