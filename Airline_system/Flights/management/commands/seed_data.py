from django.core.management.base import BaseCommand
from Flights.models import Airport, Flight

class Command(BaseCommand):
    help = "Seeds both global and Ghana-based flights and airports"

    def handle(self, *args, **kwargs):
        if Airport.objects.exists() or Flight.objects.exists():
            self.stdout.write(self.style.WARNING("⚠️ Seed skipped: Airports or Flights already exist."))
            return

        # Run the two seeding commands
        from django.core.management import call_command
        call_command('seed_flights')  # from seed_flights.py
        call_command('seedghana')     # from seedghana.py

        self.stdout.write(self.style.SUCCESS("✅ All seed data loaded successfully."))
