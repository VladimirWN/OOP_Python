from data import Node as n
from service import Operator as op
from view import View as v


def start():
    while True:
        number1 = v.View.get("Введите первое число: ")
        if is_incorrect_number(number1):
            continue
        number1 = n.Node(float(number1))

        operator = v.View.get("Выберети операцию \"+\" \"-\" \"*\" \"/\": ")
        if is_incorrect_operator(operator):
            continue
        operator = op.Operator(operator)

        number2 = v.View.get("Введите второе число: ")
        if is_incorrect_number(number2):
            continue
        number2 = n.Node(float(number2))

        v.View.set(operator.get_result(number1, number2))
        v.View.set("\nСледующий цикл.")


def is_incorrect_number(x):
    try:
        x = float(x)
        return False
    except ValueError:
        v.View.get("Введено неверное значение, повтор цикла.\n")
        return True


def is_incorrect_operator(x):
    if x in ["+", "-", "*", "/"]:
        return False
    v.View.get("Введено неверное значение, повтор цикла.\n")
    return True
