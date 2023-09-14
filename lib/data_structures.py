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

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food_dict in spicy_foods:
        if food_dict["cuisine"] == cuisine:
            return food_dict

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    heat_levels_list = list([food_item.get("heat_level") for food_item in spicy_foods])
    heat_level_avg = sum(heat_levels_list) / len(heat_levels_list)
    return heat_level_avg

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
