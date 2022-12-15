class Dish:
    def __init__(self, name: str, ingredients: dict):
        self.__name = name
        self.__ingredients = ingredients
        self.__price = round(sum([float(x.price) * float(ingredients[x]) for x in ingredients.keys()]), 2)
        self.__index = 0
        self.__item_lst = [self.__name, self.__ingredients, self.__price]

    def __str__(self):
        return "Блюдо: \"{}\", стоимость: {}\nИнгредиенты:\n{}" \
            .format(self.__name, self.__price,
                    "".join([f"\t{x[0].get_attr('name')} - {x[1]} {x[0].get_attr('type_packing')}\n"
                             for x in self.__ingredients.items()]))

    def get_attr(self, name):
        if name == "name":
            return self.__name
        elif name == "ingredients":
            return self.__ingredients
        elif name == "price":
            return self.__price
        else:
            return "Некорректный запрос"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < 3:
            i = self.__index
            self.__index += 1
            return self.__item_lst[i]
        else:
            self.__index = 0
            raise StopIteration
