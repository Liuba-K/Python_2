

def thesaurus(names_of_employees):
    key_names = []
    name = ""
    for i in names_of_employees:
        for idx, d in enumerate(key_names):
            if i[0] == d:
                name = names_of_employees[idx], i
        key_names += i[0]
        dict_names = dict(zip(key_names, names_of_employees))
        dict_names[i[0]] = name
    return dict_names


names_of_employees = ["Иван", "Мария", "Петр", "Илья"]
print(thesaurus(names_of_employees))

