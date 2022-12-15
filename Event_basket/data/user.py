class User:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Admin(User):
    def __init__(self, name, lastname, phone):
        super().__init__(name, lastname)
        self.phone = phone

    def __str__(self):
        return "Администратор- " + super().__str__() + f", номер для связи {self.phone}"


class Guest(User):
    def __init__(self, name, lastname, status):
        super().__init__(name, lastname)
        self.status = status

    def __str__(self):
        return "Гость- " + super().__str__() + f", статус участия {self.status}"
