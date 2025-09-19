from django.apps import AppConfig
import os

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        """Auto-create a superuser if it doesn't exist (safe to leave enabled)."""
        if os.environ.get("CREATE_SUPERUSER", "False") == "True":
            from django.contrib.auth import get_user_model
            from django.db.utils import OperationalError, ProgrammingError

            try:
                User = get_user_model()
                username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
                email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
                password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "adminpass")

                if not User.objects.filter(username=username).exists():
                    User.objects.create_superuser(username=username, email=email, password=password)
                    print(f"✅ Superuser '{username}' created.")
                else:
                    print(f"ℹ️ Superuser '{username}' already exists. Skipping creation.")

            except (OperationalError, ProgrammingError):
                # Happens during migrations before auth tables exist
                print("⚠️ Database not ready yet, skipping superuser creation.")
            except Exception as e:
                print(f"⚠️ Unexpected error while creating superuser: {e}")
