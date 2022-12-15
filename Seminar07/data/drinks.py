class Drinks:
    def __init__(self, name, volume):
        self.__name = name
        self.__volume = float(volume)

    def get_name(self):
        return self.__name

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume

    def __str__(self):
        return f"Напиток- {self.__name}, объемом {self.__volume}"


class HotDrinks(Drinks):
    def __init__(self, name, volume, temperature):
        super().__init__(name, volume)
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def __str__(self):
        return super().__str__() + f", температурой {self.__temperature}"


class SparklingDrinks(Drinks):
    def __init__(self, name, volume, sparkling_type):
        super().__init__(name, volume)
        self.__sparkling_type = sparkling_type

    def get_sparkling_type(self):
        return self.__sparkling_type

    def set_sparkling_type(self, sparkling_type):
        self.__sparkling_type = sparkling_type

    def __str__(self):
        return super().__str__() + f", газированность {self.__sparkling_type}"


class HotSparklingDrinks(HotDrinks):
    def __init__(self, name, volume, temperature, sparkling_type):
        super().__init__(name, volume, temperature)
        self.__sparkling_type = sparkling_type

    def __str__(self):
        return super().__str__() + f", газированность {self.__sparkling_type}"
