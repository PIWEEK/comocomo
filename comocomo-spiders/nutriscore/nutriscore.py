############
### UTIL ###
############

def get_value_of(values, symbol):
    possible = [x for x in values if x['eur_name'] == symbol]
    value = 0

    if len(possible) >= 0:
        value = float(possible[0]['best_location'])

    return value

############
## ENERGY ##
############

def _energy_beverage(value):
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
    except err:
        return 10 # > 270

def _energy_solids(value):
    REFERENCE = {
        335: 0,
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
        return next(v for (k,v) in REFERENCE.items() if value > k)
    except:
        return 0 # <= 335

def calculate_energy(values, is_beverage):
    """Calculates the NUTRISCORE value for the energy of a given
    product"""
    value = get_value_of(values, 'ENERC')

    return _energy_beverage(value) if is_beverage else _energy_solids(value)

############
## SUGARS ##
############

def _sugars_beverage(value):
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

def _sugars_solids(value):
    REFERENCE = {
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
    }

    try:
        return next(v for (k,v) in REFERENCE.items() if value > k)
    except:
        return 0 # <= 4,5

def calculate_sugars(values, is_beverage):
    """Calculates the NUTRISCORE value for the content of sugar
    in a given product"""
    value = get_value_of(values, 'SUGAR')

    return _sugars_beverage(value) if is_beverage else _sugars_solids(value)

############
## FATSAT ##
############

def calculate_fatsat(values):
    """Calculates the NUTRISCORE value for the content of saturate fat
    in a given product"""
    value = get_value_of(values, 'FATSAT')

    REFERENCE = {
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
    }

    try:
        return next(v for (k,v) in REFERENCE.items() if value > k)
    except:
        return 0 # <= 1

############
## SODIUM ##
############

def calculate_sodium(values):
    """Calculates the NUTRISCORE value for the content of sodium in a
    given product"""
    value = get_value_of(values, 'NA')

    REFERENCE = {
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
    }

    try:
        return next(v for (k,v) in REFERENCE.items() if value > k)
    except:
        return 0 # <= 1

############
## NUTRIS ##
############

def calculate_a_points(product, is_beverage):
    """Calculates nutriscore A points: Energy, sugars,
    and saturate fat"""
    values = product['values']
    energy = calculate_energy(values, is_beverage)
    sugars = calculate_sugars(values, is_beverage)
    fatsat = calculate_fatsat(values)
    sodium = calculate_sodium(values)

    return energy + sugars + fatsat + sodium

def calculate_c_points(product, is_beverage):
    """Calculates nutriscore C points: Fruits, vegetables,
    fiber and proteins"""
    fru_n_veg_solid = 0
    fru_n_veg_bever = 0
    fiber = 0
    prote = 0

    return 0

def nutriscore(product, is_beverage):
    """Calculates the NUTRISCORE of a given product"""
    pointa = calculate_a_points(product, is_beverage)
    pointc = calculate_c_points(product, is_beverage)

    return pointa + pointc


p = {'name': 'product_a',
     'values': [
         {'eur_name': 'SUGAR', 'best_location': '10'},
         {'eur_name': 'ENERC', 'best_location': '10'},
         {'eur_name': 'FATSAT', 'best_location': '10'},
         {'eur_name': 'NA', 'best_location': '10'},
     ]}

score = nutriscore(p, True)
print(score)
