from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command This command creates house rules"

    def handle(self, *args, **options):
        house_rules = [
            "Suitable for events",
            "Pets allowed",
            "Smoking allowed",
        ]
        for r in house_rules:
            HouseRule.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(house_rules)} house rules created"))
