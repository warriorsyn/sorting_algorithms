from algorithms import bubble_sort, selection_sort, insertion_sort

menus = [
    '1 - Bubble sort',
    '2 - Selection sort',
    '3 - Insertion Sort',
    '4 - Quick Sort',
    '0 - Fechar programa'
]

random_numbers = [10, 0, 24, 2, 4, 3]


def handle_menu_action(option):
    if option == 1:
        print('--------------------')
        print('BUBBLE SORT')
        print(*bubble_sort(random_numbers))
        print('--------------------')
    if option == 2:
        print('--------------------')
        print('SELECTION SORT')
        print(*selection_sort(random_numbers))
        print('--------------------')
    if option == 3:
        print('--------------------')
        print('INSERTION SORT')
        print(*insertion_sort(random_numbers))
        print('--------------------')


def __init__():
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
