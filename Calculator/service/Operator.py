class Operator:

    def __init__(self, op):
        self.operation = op

    def __addition(self, x, y):
        result = x + y
        if result == int(result):
            return int(result)
        return result

    def __subtraction(self, x, y):
        result = x - y
        if result == int(result):
            return int(result)
        return result

    def __multiplication(self, x, y):
        result = x * y
        if result == int(result):
            return int(result)
        return result

    def __division(self, x, y):
        if y == 0:
            return "На ноль делить нельзя"
        result = x / y
        if result == int(result):
            return int(result)
        return result

    def get_result(self, x, y):
        a = x.get_value()
        b = y.get_value()
        if self.operation == "+":
            return self.__addition(a, b)
        elif self.operation == "-":
            return self.__subtraction(a, b)
        elif self.operation == "*":
            return self.__multiplication(a, b)
        elif self.operation == "/":
            return self.__division(a, b)
