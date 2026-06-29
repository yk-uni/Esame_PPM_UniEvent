from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Create demo users"

    def handle(self, *args, **kwargs):

        users = [
            {
                "username": "admin_demo",
                "password": "Admin2026!",
                "role": "organizer",
                "is_staff": True,
                "is_superuser": True,
            },
            {
                "username": "organizer_demo",
                "password": "Organizer2026!",
                "role": "organizer",
            },
            {
                "username": "attendee_demo",
                "password": "Attendee2026!",
                "role": "attendee",
            },
        ]

        for u in users:

            if not User.objects.filter(username=u["username"]).exists():

                user = User.objects.create_user(
                    username=u["username"],
                    password=u["password"],
                )

                user.role = u["role"]
                user.is_staff = u.get("is_staff", False)
                user.is_superuser = u.get("is_superuser", False)
                user.save()

                self.stdout.write(
                    self.style.SUCCESS(f"Created {u['username']}")
                )

            else:

                self.stdout.write(
                    f"{u['username']} already exists"
                )