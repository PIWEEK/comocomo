############
### UTIL ###
############

def get_value_of(values, symbol):
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
    except:
        return 10 # > 270

def _energy_solids(value):
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

def calculate_energy(values, is_beverage):
    """Calculates the NUTRISCORE value for the energy of a given
    product"""
    value = get_value_of(values, 'ENERC')
    result = _energy_beverage(value) if is_beverage else _energy_solids(value)

    print(f"energy: {result} for value {value}")
    return result

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

def calculate_sugars(values, is_beverage):
    """Calculates the NUTRISCORE value for the content of sugar
    in a given product"""
    value = get_value_of(values, 'SUGAR')
    result = _sugars_beverage(value) if is_beverage else _sugars_solids(value)

    print(f"sugars: {result} for value {value}")
    return result

############
## FATSAT ##
############

def calculate_fatsat(values):
    """Calculates the NUTRISCORE value for the content of saturate fat
    in a given product"""
    value = get_value_of(values, 'FASAT')
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

    print(f"fatsat: {result} of value {value}")
    return result

############
## SODIUM ##
############

def calculate_sodium(values):
    """Calculates the NUTRISCORE value for the content of sodium in a
    given product"""
    value = get_value_of(values, 'NA')
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

    print(f"sodium: {result} of value {value}")
    return result

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

def calculate_fiber(values):
    """Calculates nutriscore C points: fibers"""
    value = get_value_of(values, 'FIBT')
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

    print(f"fiber: {result} of value {value}")
    return result

def calculate_proteins(values):
    """Calculates nutriscore C points: proteins"""
    value = get_value_of(values, 'PROT')
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

    print(f"proteins: {result} of value {value}")
    return result

def calculate_c_points(product, is_beverage, is_fruit_or_vegetable):
    """Calculates nutriscore C points: Fruits, vegetables,
    fiber and proteins"""
    values = product['values']
    # We are evaluating raw food, so an orange is supposed have 100%
    # of fruit whereas a steak has 0% of fruit
    fandv = 10 if is_fruit_or_vegetable else 0
    fiber = calculate_fiber(values)
    prote = calculate_proteins(values)

    return fandv + fiber + prote

def resolve_beverage_code(points):
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

def resolve_solid_code(points):
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

def nutriscore(product, is_beverage, is_fruit_or_vegetable):
    """Calculates the NUTRISCORE of a given product"""
    pointa = calculate_a_points(product, is_beverage)
    pointc = calculate_c_points(product, is_beverage, is_fruit_or_vegetable)
    result = pointa - pointc

    return resolve_beverage_code(result) if is_fruit_or_vegetable else resolve_solid_code(result)
