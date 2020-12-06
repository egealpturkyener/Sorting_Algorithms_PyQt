#EGE ALP TÜRKYENER
def bubble_sort(list):
    for j in range(len(list)-1):
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]: #compare the number the the next number
                list[i], list[i + 1] = list[i + 1], list[i] #according to result replace.

