class Ingredient:
    def __init__(self, name: str, category: str, type_packing: str, price: float):
        self.__name = name
        self.__category = category
        self.__type_packing = type_packing
        self.price = price
        self.__index = 0
        self.__item_lst = [self.__name, self.__category, self.__type_packing, self.price]

    def __eq__(self, other):
        return self.__name == other.__name

    def __hash__(self) -> int:
        return super().__hash__()

    def __str__(self) -> str:
        return f"{self.__name} {self.__category} {self.__type_packing} {self.price}"

    def get_attr(self, name):
        if name == "name":
            return self.__name
        elif name == "category":
            return self.__category
        elif name == "type_packing":
            return self.__type_packing
        else:
            return "Некорректный запрос"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < 4:
            i = self.__index
            self.__index += 1
            return self.__item_lst[i]
        else:
            self.__index = 0
            raise StopIteration
