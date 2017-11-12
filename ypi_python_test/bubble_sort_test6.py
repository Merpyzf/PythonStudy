def buble_sort():
    sortlist = [1, 3, 4, -1, 10, 7, 9]
    for i in range(len(sortlist) - 1):
        for j in range(len(sortlist) - i - 1):
            if sortlist[j] > sortlist[j + 1]:
                temp = sortlist[j + 1]
                sortlist[j + 1] = sortlist[j]
                sortlist[j] = temp

    return sortlist


if __name__ == '__main__':
    print buble_sort()
