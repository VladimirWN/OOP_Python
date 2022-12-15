from Seminar07.data import drinks as dr
from Seminar07.service import vending as ve
from Seminar07.view import view as vi


def start():
    drink1 = dr.HotDrinks("latte", 0.5, 90)
    drink2 = dr.HotDrinks("cappuccino", 0.3, 80)
    drink3 = dr.HotDrinks("americano", 0.3, 85)

    my_machine = ve.Vending([drink1, drink2, drink3])
    vi.View.set(f"Текущая наполненность: {print_lst(my_machine.get_drinks_list())}")
    vi.View.set(f"Продано: {my_machine.sale_drink('latte')}")
    vi.View.set(f"Текущая наполненность: {print_lst(my_machine.get_drinks_list())}\n")

    drink4 = dr.SparklingDrinks("cola", 0.5, "hard")
    drink5 = dr.HotSparklingDrinks("HOT cola", 2.0, 100, "very hard")

    my_machine.push_drinks([drink4, drink5])
    vi.View.set(f"Текущая наполненность: {print_lst(my_machine.get_drinks_list())}")
    vi.View.set(my_machine.sale_drink("cola"))
    vi.View.set(my_machine.sale_drink("americano"))
    vi.View.set(f"Текущая наполненность: {print_lst(my_machine.get_drinks_list())}")


def print_lst(lst):
    s = ""
    for i in lst:
        s += "{" + str(i[0] + 1) + "-" + str(i[1]) + "}" + "\n"
    s = s[:-1]
    return s
