import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 6),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):  # 3~ (10~17)
                random_photo = random.randint(1, 2)
                if random_photo == 1:
                    pho = f"room_photos/{random.randint(1,31)}.webp"
                else:
                    pho = f"room_photos/{random.randint(1,15)}.jpg"
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=pho,
                )

            for am in amenities:
                mnumber = random.randint(0, 15)
                if mnumber % 2 == 0:  # 왜 짝수면 추가 하는 거?
                    room.amenities.add(am)

            for fa in facilities:
                mnumber = random.randint(0, 6)
                if mnumber % 2 == 0:
                    room.facilities.add(fa)

            for ru in rules:
                mnumber = random.randint(0, 1)
                if mnumber % 2 == 0:
                    room.house_rules.add(ru)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))
