def selection(list: list[int]) -> list[int]:
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                list[min_index], list[j] = list[j], list[min_index]
    return list