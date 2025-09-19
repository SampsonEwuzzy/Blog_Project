from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser with a predefined username and password if one does not exist.'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'qwertyuiop2025')
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser "admin" already exists'))