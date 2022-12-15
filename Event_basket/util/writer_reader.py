import csv


def write_csv(file, lst: list):
    with open(f'{file}', 'w', encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerows(lst)


def read_csv(file):
    lst = list()
    with open(f'{file}', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1:
                lst.append(row)
    return lst


def write_txt(file, string):
    with open(f'{file}', 'w', encoding="UTF-8") as f:
        f.write(string)
