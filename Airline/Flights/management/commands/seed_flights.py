from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random
from Flights.models import Airport, Flight

class Command(BaseCommand):
    help = "Seed the database with 30 airports and 300 FlyDream flights"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding Airports and FlyDream Flights...")

        # (name, code, city, country)
        airport_data = [
            ("Kotoka International Airport", "ACC", "Accra", "Ghana"),
            ("Murtala Muhammed Intl", "LOS", "Lagos", "Nigeria"),
            ("Jomo Kenyatta Intl", "NBO", "Nairobi", "Kenya"),
            ("O.R. Tambo Intl", "JNB", "Johannesburg", "South Africa"),
            ("Cairo Intl", "CAI", "Cairo", "Egypt"),
            ("Dubai Intl", "DXB", "Dubai", "UAE"),
            ("Istanbul Airport", "IST", "Istanbul", "Turkey"),
            ("Heathrow Airport", "LHR", "London", "UK"),
            ("Charles de Gaulle", "CDG", "Paris", "France"),
            ("JFK International", "JFK", "New York", "USA"),

            ("King Abdulaziz Intl", "JED", "Jeddah", "Saudi Arabia"),
            ("Changi Airport", "SIN", "Singapore", "Singapore"),
            ("Incheon Intl", "ICN", "Seoul", "South Korea"),
            ("Frankfurt Airport", "FRA", "Frankfurt", "Germany"),
            ("Amsterdam Schiphol", "AMS", "Amsterdam", "Netherlands"),
            ("Madrid Barajas", "MAD", "Madrid", "Spain"),
            ("Zurich Airport", "ZRH", "Zurich", "Switzerland"),
            ("Rome Fiumicino", "FCO", "Rome", "Italy"),
            ("Doha Hamad Intl", "DOH", "Doha", "Qatar"),
            ("Abu Dhabi Intl", "AUH", "Abu Dhabi", "UAE"),
            ("Sydney Airport", "SYD", "Sydney", "Australia"),
            ("Toronto Pearson", "YYZ", "Toronto", "Canada"),
            ("Beijing Capital", "PEK", "Beijing", "China"),
            ("San Francisco Intl", "SFO", "San Francisco", "USA"),
            ("Cape Town Intl", "CPT", "Cape Town", "South Africa"),
            ("Casablanca Mohamed V", "CMN", "Casablanca", "Morocco"),
            ("Dakar Blaise Diagne", "DSS", "Dakar", "Senegal"),
            ("Kigali Intl", "KGL", "Kigali", "Rwanda"),
            ("Addis Ababa Bole", "ADD", "Addis Ababa", "Ethiopia"),
            ("Kuala Lumpur Intl", "KUL", "Kuala Lumpur", "Malaysia"),
        ]

        travel_classes = ["economy", "business", "first"]

        # Optional: clear existing data
        Flight.objects.all().delete()
        Airport.objects.all().delete()

        # Create airports
        airports = []
        for name, code, city, country in airport_data:
            airport = Airport.objects.create(
                name=name,
                code=code,
                city=city,
                country=country
            )
            airports.append(airport)

        # Create 300 flights
        for _ in range(300):
            origin, destination = random.sample(airports, 2)
            days_ahead = random.randint(1, 60)
            departure_time = timezone.now() + timedelta(days=days_ahead, hours=random.randint(5, 23))
            arrival_time = departure_time + timedelta(hours=random.randint(2, 8))
            price = round(random.uniform(150, 1200), 2)

            Flight.objects.create(
                flight_number=f"FD{random.randint(1000,9999)}",
                origin=origin,
                destination=destination,
                departure_time=departure_time,
                arrival_time=arrival_time,
                price=price,
                travel_class=random.choice(travel_classes)
            )

        self.stdout.write(self.style.SUCCESS("✅ 30 Airports and 300 FlyDream flights seeded successfully."))
