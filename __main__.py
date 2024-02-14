def remove_duplicates(_name_sets: list):
    for name in _name_sets:
        if _name_sets.count(name) > 1:
            _name_sets.remove(name)


def remove_subsets(_name_sets: list):
    i = 0

    while i < len(_name_sets):
        name = _name_sets[i]
        subsets = tuple(
            filter(lambda x: name.issubset(x) and (name != x), _name_sets))

        if len(subsets) > 0:
            _name_sets.remove(name)
            continue

        i += 1


def main():
    input_data = ["Иванов Илья Сергеевич", "Иванов Илья", "Илья Иванов",
                  "Илья",
                  "Егоров Андрей Михайлович", "Андрей", "Егоров Андрей",
                  "Михаил Сергеевич", "Сергеевич Михаил"]

    # Каст всех элементов исходного списка в set (множества)
    name_list = list(map(lambda name: set(name.split(" ")), input_data))

    # Фильтр на "одиночные имена"
    name_sets = filter(lambda name: len(name) > 1, name_list)

    name_sets = list(name_sets)

    # Удаляем дубликаты без учёта порядка
    remove_duplicates(name_sets)

    # Удаляем подмножества ФИО/ФИ
    remove_subsets(name_sets)

    # Итоговый список имён без дубликатов и неполных вариантов
    names = list(map(lambda name: input_data[name_list.index(name)],
                     name_sets))

    print(names)


if __name__ == "__main__":
    main()
