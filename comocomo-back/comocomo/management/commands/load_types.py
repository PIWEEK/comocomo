import json

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
        file_text = input_file.read()
        file_json = json.loads(file_text)
        products = file_json['products']
        for product in products:
            name = product['ori_name'],
            score = self.nutriscore(product, is_drink, is_fruit)
            # Creating food kind
            FoodType.objects.create(
                kind = food_kind,
                name = name[0],
                nutriscore = score
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully created {len(products)} food entries"))

    ############
    ### UTIL ###
    ############

    def get_value_of(self, values, symbol):
        possible = [x for x in values if x['eur_name'] == symbol]
        value = 0
        try:
            value = float(possible[0].get('best_location', '0'))
        except:
            value = 0

        return value

    ############
    ## ENERGY ##
    ############

    def _energy_beverage(self, value):
        REFERENCE = {
            0: 0,
            30: 1,
            60: 2,
            90: 3,
            120: 4,
            150: 5,
            180: 6,
            210: 7,
            240: 8,
            270: 9
        }

        try:
            return next(v for (k,v) in REFERENCE.items() if value <= k)
        except:
            return 10 # > 270

    def _energy_solids(self, value):
        REFERENCE = {
        335: 1,
            670: 2,
            1005: 3,
            1340: 4,
            1675: 5,
            2010: 6,
            2345: 7,
            2680: 8,
            3015: 9,
            3350: 10
        }

        try:
            return next(v for (k,v) in sorted(REFERENCE.items(), reverse=True) if value > k)
        except:
            return 0 # <= 335

    def calculate_energy(self, values, is_beverage):
        """Calculates the NUTRISCORE value for the energy of a given
        product"""
        value = self.get_value_of(values, 'ENERC')
        result = self._energy_beverage(value) if is_beverage else self._energy_solids(value)

        return result

    ############
    ## SUGARS ##
    ############

    def _sugars_beverage(self, value):
        REFERENCE = {
            0: 0,
            1.5: 1,
            3: 2,
            4.5: 3,
            6: 4,
            7.5: 5,
            9: 6,
            10.5: 7,
            12: 8,
            13.5: 9
        }

        try:
            return next(v for (k,v) in REFERENCE.items() if value <= k)
        except:
            return 10 # > 13.5

    def _sugars_solids(self, value):
        REFERENCE = sorted({
        4.5: 1,
            9: 2,
            13.5: 3,
            18: 4,
            22.5: 5,
            27: 6,
            31: 7,
            36: 8,
            40: 9,
            45: 10
        }.items(), reverse=True)

        try:
            return next(v for (k,v) in REFERENCE if value > k)
        except:
            return 0 # <= 4,5

    def calculate_sugars(self, values, is_beverage):
        """Calculates the NUTRISCORE value for the content of sugar
        in a given product"""
        value = self.get_value_of(values, 'SUGAR')
        result = self._sugars_beverage(value) if is_beverage else self._sugars_solids(value)

        return result

    ############
    ## FATSAT ##
    ############

    def calculate_fatsat(self, values):
        """Calculates the NUTRISCORE value for the content of saturate fat
        in a given product"""
        value = self.get_value_of(values, 'FASAT')
        result = 0

        REFERENCE = sorted({
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10
        }.items(), reverse=True)

        try:
            result = next(v for (k,v) in REFERENCE if value > k)
        except:
            result = 0 # <= 1

        return result

    ############
    ## SODIUM ##
    ############

    def calculate_sodium(self, values):
        """Calculates the NUTRISCORE value for the content of sodium in a
        given product"""
        value = self.get_value_of(values, 'NA')
        result = 0

        REFERENCE = sorted({
            90: 1,
            180: 2,
            270: 3,
            360: 4,
            450: 5,
            540: 6,
            630: 7,
            720: 8,
            810: 9,
            900: 10
        }.items(), reverse=True)

        try:
            result = next(v for (k,v) in REFERENCE if value > k)
        except:
            result = 0 # <= 1

        return result

    ############
    ## NUTRIS ##
    ############

    def calculate_a_points(self, product, is_beverage):
        """Calculates nutriscore A points: Energy, sugars,
        and saturate fat"""
        values = product['values']
        energy = self.calculate_energy(values, is_beverage)
        sugars = self.calculate_sugars(values, is_beverage)
        fatsat = self.calculate_fatsat(values)
        sodium = self.calculate_sodium(values)

        return energy + sugars + fatsat + sodium

    def calculate_fiber(self, values):
        """Calculates nutriscore C points: fibers"""
        value = self.get_value_of(values, 'FIBT')
        result = 0

        REFERENCE = sorted({
            0.7: 1,
            1.4: 2,
            2.1: 3,
            2.8: 4,
            3.5: 5
        }.items(), reverse=True)

        try:
            result = next(v for (k,v) in REFERENCE if value > k)
        except:
            result =0 # <= 0.7

        return result

    def calculate_proteins(self, values):
        """Calculates nutriscore C points: proteins"""
        value = self.get_value_of(values, 'PROT')
        result = 0

        REFERENCE = sorted({
            1.6: 1,
            3.2: 2,
            4.8: 3,
            6.4: 4,
            8.0: 5
        }.items(), reverse=True)

        try:
            result = next(v for (k,v) in REFERENCE if value > k)
        except:
            result = 0 # <= 1.6

        return result

    def calculate_c_points(self, product, is_beverage, is_fruit_or_vegetable):
        """Calculates nutriscore C points: Fruits, vegetables,
        fiber and proteins"""
        values = product['values']
        # We are evaluating raw food, so an orange is supposed have 100%
        # of fruit whereas a steak has 0% of fruit
        fandv = 10 if is_fruit_or_vegetable else 0
        fiber = self.calculate_fiber(values)
        prote = self.calculate_proteins(values)

        return fandv + fiber + prote

    def resolve_beverage_code(self, points):
        if points < -15:
            return 'A'
        elif -15 <= points <= 1:
            return 'B'
        elif 2 <= points <= 5:
            return 'C'
        elif 6 <= points <= 9:
            return 'D'
        else:
            return 'E'

    def resolve_solid_code(self, points):
        if -15 <= points <= -1:
            return 'A'
        elif 0 <= points <= 2:
            return 'B'
        elif 3 <= points <= 10:
            return 'C'
        elif 11 <= points <= 18:
            return 'D'
        else:
            return 'E'

    def nutriscore(self, product, is_beverage, is_fruit_or_vegetable):
        """Calculates the NUTRISCORE of a given product"""
        pointa = self.calculate_a_points(product, is_beverage)
        pointc = self.calculate_c_points(product, is_beverage, is_fruit_or_vegetable)
        result = pointa - pointc

        return self.resolve_beverage_code(result) if is_fruit_or_vegetable else self.resolve_solid_code(result)
