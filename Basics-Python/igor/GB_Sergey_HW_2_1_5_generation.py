def sum_digit(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result


def summ_multiple_seven(handle_list):
    free_list = [item for item in handle_list if sum_digit(item) % 7 == 0]
    summ_free_list = 0
    for item in free_list:
        summ_free_list += item
    return summ_free_list


list_task_1 = [number ** 3 for number in range(1, 1001) if number % 2 != 0]
print(summ_multiple_seven(list_task_1))

list_task_2 = [item + 17 for item in list_task_1]
print(summ_multiple_seven(list_task_2))
