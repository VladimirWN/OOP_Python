class Vending:
    def __init__(self, lst):
        self.__drinks_list = lst

    def push_drinks(self, lst):
        self.__drinks_list.extend(lst)

    def sale_drink(self, name):
        for i in range(len(self.__drinks_list)):
            if self.__drinks_list[i].get_name() == name:
                return self.__drinks_list.pop(i)

    def get_drinks_list(self):
        return enumerate(self.__drinks_list)
