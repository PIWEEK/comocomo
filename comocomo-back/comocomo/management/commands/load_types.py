from django.core.management.base import BaseCommand, CommandError
from gathering.models import FoodKind, FoodType

class Command(BaseCommand):
    help = 'Load a json file with food types in the database'

    def add_arguments(self, parser):
        parser.add_argument('food_kind', type=int,
                help='ID of food kind associated to this file')
        parser.add_argument('file_path', type=str,
                help='Full path to the json file')
        parser.add_argument('-d', '--is-drink', action='store_true',
                help='The contents of the file are drinks')
        parser.add_argument('-f', '--is-fruit', action='store_true',
                help='The contents of the file are fruits')

    def handle(self, *args, **options):
        food_kind = FoodKind.objects.get(id = options['food_kind'])
        self.load_file(
            food_kind,
            options['file_path'],
            options['is_drink'],
            options['is_fruit'],
        )
        self.stdout.write(self.style.SUCCESS('Successfully imported file'))

    def load_file(self, food_kind, file_path, is_drink, is_fruit):
        input_file = open(file_path)
        # TODO...

