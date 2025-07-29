# flights/management/commands/seedghana.py

from django.core.management.base import BaseCommand
from Flights.models import Airport, Flight
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Seed Ghana-based airports and flights for testing'

    def handle(self, *args, **kwargs):

        # Ghanaian airports
        ghana_airports_data = [
            {"name": "Kotoka International Airport", "city": "Accra", "code": "ACC"},
            {"name": "Kumasi International Airport", "city": "Kumasi", "code": "KMS"},
            {"name": "Tamale Airport", "city": "Tamale", "code": "TML"},
            {"name": "Takoradi Airport", "city": "Takoradi", "code": "TKD"},
        ]

        ghana_airports = []
        for data in ghana_airports_data:
            airport, _ = Airport.objects.get_or_create(
                code=data["code"],
                defaults={
                    "name": data["name"],
                    "city": data["city"],
                    "country": "Ghana"
                }
            )
            ghana_airports.append(airport)

        # International destinations
        intl_airports_data = [
            ("Murtala Muhammed Intl", "Lagos", "LOS", "Nigeria"),
            ("Abidjan Intl", "Abidjan", "ABJ", "Côte d'Ivoire"),
            ("Jomo Kenyatta Intl", "Nairobi", "NBO", "Kenya"),
            ("Dubai Intl", "Dubai", "DXB", "UAE"),
            ("Heathrow Airport", "London", "LHR", "UK"),
            ("JFK Intl Airport", "New York", "JFK", "USA"),
        ]

        intl_airports = []
        for name, city, code, country in intl_airports_data:
            airport, _ = Airport.objects.get_or_create(
                code=code,
                defaults={"name": name, "city": city, "country": country}
            )
            intl_airports.append(airport)

        all_airports = ghana_airports + intl_airports

        today = timezone.now()
        flight_classes = ['economy', 'business']

        # Domestic flights
        for i in range(20):
            origin = random.choice(ghana_airports)
            destination = random.choice([a for a in ghana_airports if a != origin])
            Flight.objects.create(
                flight_number=f"FDG{100+i}",
                origin=origin,
                destination=destination,
                departure_time=today + timedelta(days=random.randint(1, 15)),
                arrival_time=today + timedelta(days=random.randint(1, 15), hours=1),
                travel_class=random.choice(flight_classes),
                price=random.choice([150, 180, 200, 250])
            )

        # International flights from Ghana
        accra = Airport.objects.get(code="ACC")
        for i, dest in enumerate(intl_airports):
            Flight.objects.create(
                flight_number=f"FDG{200+i}",
                origin=accra,
                destination=dest,
                departure_time=today + timedelta(days=random.randint(3, 20)),
                arrival_time=today + timedelta(days=random.randint(3, 20), hours=6),
                travel_class=random.choice(flight_classes),
                price=random.choice([500, 700, 850, 1000, 1200])
            )

        self.stdout.write(self.style.SUCCESS("✅ Ghana flights seeded successfully."))