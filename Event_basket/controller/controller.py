from Event_basket.data.user import *
from Event_basket.service.event import *
from Event_basket.service.product_service import *
from Event_basket.view.console_view import *
from Event_basket.view.menu import *


def start():
    db_ingredients = load_ingredient_list()
    db_dishes = load_dish_list()

    point = -1
    while point != 0:
        menu()
        point = menu_inp()
        if point == 1:
            for i in db_ingredients:
                sent_msg(i)
        elif point == 2:
            for i in db_dishes:
                sent_msg(i)
        elif point == 3:
            new_i = add_ingredient()
            if new_i not in db_ingredients:
                db_ingredients.append(new_i)
                update_ingredient_list(db_ingredients)
            else:
                sent_msg("такой ингредент уже есть, отмена.")
        elif point == 4:
            pass
        elif point == 5:
            pass
        elif point == 6:
            pass
        elif point == 7:
            pass
        if point != 0:
            input('Для возврата в главное меню введите любой символ.\n')
    else:
        print('Завершение работы программы.')


def add_ingredient():
    name = get_data("Введите название (только буквы): ")
    while not is_correct_str(name):
        sent_msg("Некорректный ввод, повторите: ")
        name = get_data()

    sent_msg("Введите номер категории: ")
    while True:
        for i in Category:
            sent_msg(f"{i.value} - {i.name}")
        category = get_data()
        if not is_correct_number(category):
            sent_msg("Некорректный ввод, повторите: ")
            continue
        if int(category) not in range(0, 9):
            sent_msg("Некорректный ввод, повторите: ")
        else:
            break

    sent_msg("Введите номер типа упаковки: ")
    while True:
        for i in TypeOfPackaging:
            sent_msg(f"{i.value} - {i.name}")
        type_packing = get_data()
        if not is_correct_number(type_packing):
            sent_msg("Некорректный ввод, повторите: ")
            continue
        if int(type_packing) not in range(0, 3):
            sent_msg("Некорректный ввод, повторите: ")
        else:
            break

    price = get_data("Введите цену за единицу (кг): ")
    while not is_correct_number(price):
        sent_msg("Некорректный ввод, повторите: ")
        price = get_data()
    return new_ingredient(name, category, type_packing, price)
