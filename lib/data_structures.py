import ipdb
heat_icon = "🌶"

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [ food_item.get("name") for food_item in spicy_foods ]


def get_spiciest_foods(spicy_foods):
    return [ dict_item for dict_item in spicy_foods if dict_item.get("heat_level") > 5 ]

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print('{} ({}) | Heat Level: {}'.format(item.get("name"), item.get("cuisine"), item.get("heat_level") * heat_icon))

ipdb.set_trace()
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
