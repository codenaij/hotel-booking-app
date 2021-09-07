from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = 'This command creates room types'

    def handle(self, *args, **kwargs):
        room_types = [
            "Hotel Room",
            "Shared Room",
            "Private Room",
            "Entire Space",
        ]
        for rt in room_types:
            RoomType.objects.create(name=rt)
        self.stdout.write(self.style.SUCCESS(f"{len(room_types)} room types created"))
