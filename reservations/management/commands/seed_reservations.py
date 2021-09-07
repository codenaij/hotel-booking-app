import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = 'This command creates reservations'

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=1, help="Number of reservations to create")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(reservation_models.Reservation, number, {
            "guest": lambda x: random.choice(users),
            "room": lambda x: random.choice(rooms),
            "check_in": lambda x: datetime.now(),
            "check_out": lambda x: datetime.now() + timedelta(days=random.randint(3, 10)),
            "status": lambda x: random.choice(["pending", "confirmed", "canceled"])
        })
        
        seeder.execute()
     
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created"))
