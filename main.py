from itertools import combinations

equipment = {
    'в': (3, 25),
    'п': (2, 15),
    'б': (2, 15),
    'а': (2, 20),
    'и': (1, 5),
    'н': (1, 15),
    'т': (3, 20),
    'о': (1, 25),
    'ф': (1, 15),
    'д': (1, 10),
    'к': (2, 20),
    'р': (2, 20)
}


def max_search(equipment_dict=None, bp_len=3, bp_width=3, start_value=15):
    if equipment_dict is None:
        equipment_dict = equipment
    new_dict = {}
    for amount in range(1, len(equipment_dict) - 1):
        variable = ["".join(map(str, comb)) for comb in combinations(equipment_dict, amount)]
        for letters in variable:
            new_letters = ''
            area = 0
            value = 0
            letters_from_dict = list(equipment_dict.keys())
            for letter in letters:
                new_letters += letter * equipment_dict[letter][0]
                letters_from_dict.remove(letter)
                area += equipment_dict[letter][0]
                value += equipment_dict[letter][1]
            for letter in letters_from_dict:
                value -= equipment_dict[letter][1]
            value += start_value
            if area <= bp_len * bp_width and value > 0:
                new_dict[letters] = (value, area, new_letters)
    new_list = sorted(new_dict.values(), reverse=True)
    txt_to_print = ''
    last_width = 0
    if new_list:
        for index in range(len(new_list[0][2])):
            txt_to_print += f'[{new_list[0][2][index]}] '
            if (index + 1) // bp_width > last_width:
                last_width += 1
                txt_to_print += '\n'
        print(f'Наилучший вариант:\n'
              '{txt_to_print}'
              'Итоговые очки выживания: {new_list[0][0]}\n\n')
    else:
        print('Вариантов, соответствующих условию задачи не найдено\n\n')
    return new_list


# Все комбинации
result = max_search()
print(f'Все комбинации:'
      f'(очки выживания, количетсов мест, комбинация'
      f'{result}\n\n')

# Для 7 ячеек
print('Для 7 ячеек:')
max_search(bp_width=7, bp_len=1)
