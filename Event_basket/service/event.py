from Event_basket.util.writer_reader import *


class Event:
    def __init__(self, name: str, date: str, users: list, basket: dict):
        self.__name = name
        self.date = date
        self.__users = users
        self.__product_basket = basket

    def __str__(self):
        return "Название мероприятия: {}, дата проведения {}\n" \
               "список участников:\n{}" \
               "блюда на мероприятие:\n{}" \
               "стоимость закупки продуктов: {}" \
            .format(self.__name, self.date,
                    "".join([f"\t{x}\n" for x in self.__users]),
                    "".join([f"\t{x[0].get_attr('name')} {x[1]} шт.\n" for x in self.__product_basket.items()]),
                    sum([dish[0].get_attr('price') * dish[1] for dish in self.__product_basket.items()]))

    def export_txt_purchase_list(self, file):
        write_txt(file, self.get_total_products_purchase())

    def get_total_products_purchase(self):
        ingredient_lst = dict()
        for dish in self.__product_basket.items():
            for ingredient in dish[0].get_attr('ingredients').items():
                if ingredient[0] not in ingredient_lst.keys():
                    ingredient_lst.setdefault(ingredient[0], dish[1] * ingredient[1])
                else:
                    ingredient_lst[ingredient[0]] = ingredient_lst.get(ingredient[0]) + dish[1] * ingredient[1]

        sorted_by_category = dict()
        for ingredient in ingredient_lst.items():
            if ingredient[0].get_attr('category') not in sorted_by_category.keys():
                sorted_by_category.setdefault(ingredient[0].get_attr('category'), list())
                sorted_by_category[ingredient[0].get_attr('category')].append(ingredient)
            else:
                sorted_by_category[ingredient[0].get_attr('category')].append(ingredient)

        total_price = round(sum([x[0].price * x[1] for x in ingredient_lst.items()]), 2)

        return "Список продуктов для закупки:\n{}итоговая стоимость: {}" \
            .format("".join([f"\t{item_from_sorted_by_category[0]}\n" +
                             "".join([f"\t\t{ingredient[0].get_attr('name')} - "
                                      f"{round(ingredient[1], 2)} {ingredient[0].get_attr('type_packing')}, "
                                      f"стоимость {round(ingredient[0].price * ingredient[1], 2)}\n"
                                      for ingredient in item_from_sorted_by_category[1]])
                             for item_from_sorted_by_category in sorted_by_category.items()]), total_price)
