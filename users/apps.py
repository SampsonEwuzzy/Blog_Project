from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        # Auto-create superuser if CREATE_SUPERUSER=True is set in Render env vars
        if os.environ.get("CREATE_SUPERUSER", "False") == "True":
            try:
                User = get_user_model()
                username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
                email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
                password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "adminpass")

                if not User.objects.filter(username=username).exists():
                    User.objects.create_superuser(
                        username=username, email=email, password=password
                    )
                    print("✅ Superuser created!")
            except Exception as e:
                # Prevent crashes if migrations aren't ready yet
                print(f"⚠️ Could not create superuser: {e}")
