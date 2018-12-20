from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from gathering.models import FoodKind

class Command(BaseCommand):
    help = 'Create the default food kinds'

    def handle(self, *args, **kwargs):

        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE "{0}" RESTART IDENTITY CASCADE'.format(FoodKind._meta.db_table))

        FoodKind.objects.create(
            name = 'Lácteos',
            description = 'Lácteos y derivados',
            icon_name = 'lacteos.svg'
        )

        FoodKind.objects.create(
            name = 'Huevos',
            description = 'Huevos y derivados',
            icon_name = 'huevos.svg'
        )

        FoodKind.objects.create(
            name = 'Cárnicos',
            description = 'Cárnicos y derivados',
            icon_name = 'carnicos.svg'
        )

        FoodKind.objects.create(
            name = 'Pescados y mariscos',
            description = 'Pescados, moluscos, reptiles, crustáceos y derivados',
            icon_name = 'pescados_y_mariscos.svg'
        )

        FoodKind.objects.create(
            name = 'Grasas y aceites',
            description = 'Grasas y aceites',
            icon_name = 'grasas_y_aceites.svg'
        )

        FoodKind.objects.create(
            name = 'Cereales',
            description = 'Cereales y derivados',
            icon_name = 'cereales.svg'
        )

        FoodKind.objects.create(
            name = 'Legumbres y frutos secos',
            description = 'Legumbres, semillas, frutos secos y derivados',
            icon_name = 'legumbres_y_frutos_secos.svg'
        )

        FoodKind.objects.create(
            name = 'Verduras y hortalizas',
            description = 'Verduras, hortalizas y derivados',
            icon_name = 'verduras_y_hortalizas.svg'
        )

        FoodKind.objects.create(
            name = 'Frutas',
            description = 'Frutas y derivados',
            icon_name = 'frutas.svg'
        )

        FoodKind.objects.create(
            name = 'Dulces y chocolates',
            description = 'Azúcar, chocolate y derivados',
            icon_name = 'dulces_y_chocolates.svg'
        )

        FoodKind.objects.create(
            name = 'Bebidas',
            description = 'Bebidas (no lácteas)',
            icon_name = 'bebidas.svg'
        )

        FoodKind.objects.create(
            name = 'Miscelánea',
            description = 'Miscelánea',
            icon_name = 'miscelanea.svg'
        )

        self.stdout.write(self.style.SUCCESS('Successfully created 12 food kinds'))

