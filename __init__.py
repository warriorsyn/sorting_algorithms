import random
from algorithms import bubble_sort, selection_sort, insertion_sort, quick_sort

menus = [
    '1 - Bubble sort',
    '2 - Selection sort',
    '3 - Insertion Sort',
    '4 - Quick Sort',
    '0 - Fechar programa'
]


def handle_menu_action(option, data):
    if option == 1:
        print('--------------------')
        print('BUBBLE SORT')
        print(*bubble_sort(data))
        print('--------------------')
    if option == 2:
        print('--------------------')
        print('SELECTION SORT')
        print(*selection_sort(data))
        print('--------------------')
    if option == 3:
        print('--------------------')
        print('INSERTION SORT')
        print(*insertion_sort(data))
        print('--------------------')
    if option == 4:
        print('--------------------')
        print('QUICK SORT')
        print(*quick_sort(data, 0, len(data) - 1))
        print('--------------------')


def __init__():
    numbers_choose = input("Escolha uma série do números separados por ',' para serem ordenados: ")

    splited = numbers_choose.split(',')

    map_object = map(int, splited)

    integers_list = list(map_object)

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
        handle_menu_action(option, integers_list)


__init__()
