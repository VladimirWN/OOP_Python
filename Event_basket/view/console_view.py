def sent_msg(message):
    print(message)


def get_data(message=None):
    if message is None:
        return input()
    return input(message)
