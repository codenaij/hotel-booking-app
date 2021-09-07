from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = 'This command creates facilities'

    def handle(self, *args, **kwargs):
        facilities = [
            "Private Entrance",
            "Paid Parking on Premises",
            "Paid Parking off premises",
            "Elevator",
            "Parking",
            "Gym"
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created"))
