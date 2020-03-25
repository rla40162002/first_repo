from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command This command creates room types"

    def handle(self, *args, **options):
        room_types = [
            "Entire place",
            "Private room",
            "Hotel room",
            "Shared room",
        ]
        for t in room_types:
            RoomType.objects.create(name=t)
        self.stdout.write(self.style.SUCCESS(f"{len(room_types)} room types created"))
