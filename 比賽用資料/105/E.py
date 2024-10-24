def binary(i):
    if i*2+1 >= n: return True
    if i*2+2 >= n: return True
    return  lst[i*2+1] < lst[i] < lst[i*2+2] and binary(i*2+1) and binary(i*2+2)


def max_heap(i):
    if i*2+1 >= n: return True
    if i*2+2 >= n: return True
    return lst[i*2+1] < lst[i] and lst[i*2+2] < lst[i] and max_heap(i*2+1) and max_heap(i*2+2)

def min_heap(i):
    if i*2+1 >= n: return True
    if i*2+2 >= n: return True
    return lst[i*2+1] > lst[i] and lst[i*2+2] > lst[i] and min_heap(i*2+1) and max_heap(i*2+2)


for _ in range(int(input())):
    lst = list(eval(input()))
    n = len(lst)
    if binary(0):
        print('B')
    elif min_heap(0) or max_heap(0):
        print('H')
    else:
        print('F')