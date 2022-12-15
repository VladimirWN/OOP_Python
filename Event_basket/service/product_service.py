from Event_basket.data.ingredient import *
from Event_basket.data.enum_product import *
from Event_basket.data.dish import *
from Event_basket.util.writer_reader import *


def new_ingredient(name: str, category: int, type_packing: int, price: float):
    for i in Category:
        if int(category) == i.value:
            category = i.name
            break
    for i in TypeOfPackaging:
        if int(type_packing) == i.value:
            type_packing = i.name
            break
    return Ingredient(name, category, type_packing, price)


def is_correct_str(value: str):
    return value.isalpha()


def is_correct_number(value: str):
    try:
        value = float(value)
        return True
    except ValueError:
        return False


def new_dish(name: str, ingredients: dict):
    return Dish(name, ingredients)


def load_ingredient_list():
    lst = read_csv("ingredients.csv")
    ingredient_lst = list()
    for i in lst:
        ingredient_lst.append(Ingredient(i[0], i[1], i[2], i[3]))
    return ingredient_lst


def load_dish_list():
    lst = read_csv("dishes.csv")
    dish_lst = list()
    ingredient_lst = load_ingredient_list()
    for i in lst:
        current_ingredient = dict()
        for j in i[1].split(","):
            for k in ingredient_lst:
                if j.split(":")[0] == k.get_attr('name'):
                    current_ingredient.setdefault(k, float(j.split(":")[1]))
                    break
        dish_lst.append(Dish(i[0], current_ingredient))
    return dish_lst


def update_ingredient_list(lst: list):
    write_csv("ingredients.csv", lst)


def update_dish_list(lst: list):
    lst_for_update = list()
    for i in lst:
        s = list()
        s.append(i.get_attr('name'))
        s.append(",".join([f"{x[0].get_attr('name')}:{x[1]}" for x in i.get_attr('ingredients').items()]))
        s.append(str(i.get_attr('price')))
        lst_for_update.append(s)
    write_csv("dishes.csv", lst_for_update)
