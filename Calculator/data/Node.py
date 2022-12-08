class Node:
    def __init__(self, x):
        if x == int(x):
            self.__x = int(x)
        else:
            self.__x = x

    def get_value(self):
        return self.__x
