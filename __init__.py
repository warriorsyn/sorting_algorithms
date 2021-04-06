import random
from algorithms import bubble_sort, selection_sort, insertion_sort, quick_sort

menus = [
    '1 - Bubble sort',
    '2 - Selection sort',
    '3 - Insertion Sort',
    '4 - Quick Sort',
    '0 - Fechar programa'
]

random_numbers = []


def generate_random_numbers(quantity):
    random_numbers.clear()
    for i in range(0, quantity):
        random_numbers.append(random.randint(1, 100))


def handle_menu_action(option):
    if option == 1:
        print('--------------------')
        print('BUBBLE SORT')
        generate_random_numbers(10)
        print(*bubble_sort(random_numbers))
        print('--------------------')
    if option == 2:
        print('--------------------')
        print('SELECTION SORT')
        generate_random_numbers(10)
        print(*selection_sort(random_numbers))
        print('--------------------')
    if option == 3:
        print('--------------------')
        print('INSERTION SORT')
        generate_random_numbers(10)
        print(*insertion_sort(random_numbers))
        print('--------------------')
    if option == 4:
        print('--------------------')
        print('QUICK SORT')
        generate_random_numbers(10)
        print(*quick_sort(random_numbers, 0, len(random_numbers) - 1))
        print('--------------------')


def __init__():
    generate_random_numbers(10)
    while True:
        for menu in menus:
            print(menu)

        try:
            option = int(input("Escolha uma das opções acima: "))
            menu[option]
        except Exception as e:
            print("Opção inválida, por favor escolha outra opção")

        if not option:
            break
        handle_menu_action(option)


__init__()
