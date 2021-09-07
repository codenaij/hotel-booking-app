from django.core.management.base import BaseCommand
from rooms.models import Amenity
# from rooms import models as room_models


class Command(BaseCommand):

    help = 'This command creates amenities'

    # def add_arguments(self, parser):
    #    parser.add_argument(

    #    )

    def handle(self, *args, **kwargs):
        amenities = [
            'Air Conditioning',
            'Alarm Clock',
            'Balcony',
            'Bathroom',
            'Bathtub',
            'Bed Linen',
            'Boating',
            'Cable TV',
            'Carbon Monoxide Detectors',
            'Chairs',
            'Children Area',
            'Coffee Maker in Room',
            'Cooking Hob',
            'Cookware & Kitchen Utensils',
            'Dishwasher',
            'Double Bed',
            'En suite bathroom',
            'Free Parking',
            'Free wireless internet',
            'Freezer',
            'Fridge / Freezer',
            'Golf',
            'Hair Dryer',
            'Heating',
            'Hot tub',
            'Indoor Pool',
            'Ironing Board',
            'Microwave',
            'Outdoor Pool',
            'Outdoor Tennis',
            'Oven',
            'Queen size bed',
            'Restaurant',
            'Shopping Mall',
            'Shower',
            'Smoke detectors',
            'Sofa',
            'Stereo',
            'Swimming Pool',
            'Toilet',
            'Towels',
            'TV',
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities Created"))
