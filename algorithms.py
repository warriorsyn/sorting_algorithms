import time

random_numbers = [10, 0, 24, 2, 4, 3]


# measure decorator

def measure(func):
    def inner(*args):
        start_time = time.time()
        ags = func(*args)
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(f"Elapsed time was {time_elapsed}")
        return args[0]

    return inner


# Bubble sort
@measure
def bubble_sort(numbers) -> list:
    time.sleep(1)
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                ordered = False
    return numbers


# Selection Sort

@measure
def selection_sort(numbers):
    time.sleep(1)
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


# Insertion sort

@measure
def insertion_sort(numbers):
    time.sleep(1)
    for i in range(1, len(numbers)):
        aux = numbers[i]
        k = i - 1

        while k >= 0 and numbers[k] > aux:
            numbers[k + 1] = numbers[k]
            k -= 1

        numbers[k + 1] = aux

    return numbers
