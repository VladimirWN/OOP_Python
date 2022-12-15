class View:
    @staticmethod
    def set(message):
        print(message)

    @staticmethod
    def get(message):
        return input(message)

    @staticmethod
    def get():
        return input()
