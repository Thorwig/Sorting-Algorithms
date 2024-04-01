def myinsertion(list: list[int]) -> list[int]:
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j]<list[j-1]:
                 list[j-1], list[j] = list[j],list[j-1]
    return list

def insertion(list: list[int]) -> list[int]:
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and list[j] > temp:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list