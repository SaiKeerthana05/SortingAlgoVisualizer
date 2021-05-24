### HEAP SORT ###

import time
from Sorting_Visualizer.colors import *


def heapify(array, n, i, drawArray, timeTick,set):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        drawArray(array, [RED if x == i or x == largest else BLUE if x > set else ORANGE for x in range(len(array))])
        time.sleep(timeTick/3)
        array[i], array[largest] = array[largest], array[i]
        drawArray(array, [RED if x == i or x == largest else BLUE if  x > set else ORANGE for x in range(len(array))])
        drawArray(array, [LIGHT_GREEN if x == i or x == largest else BLUE if x > set else ORANGE for x in range(len(array))])
        time.sleep(timeTick/3)
        drawArray(array,[BLUE if x > set else ORANGE for x in range(len(array))])
        heapify(array, n, largest, drawArray, timeTick,set)


def heap_sort(array, drawArray, timeTick):
    n = len(array)

    for i in range(n - 1, -1, -1):
        heapify(array, n, i, drawArray, timeTick,n)

    for i in range(n - 1, 0, -1):
        drawArray(array, [YELLOW if x == i else PURPLE if x == 0 else BLUE if x > i else ORANGE for x in range(len(array))])
        time.sleep(timeTick/4)
        array[i], array[0] = array[0], array[i]
        time.sleep(timeTick/2)
        drawArray(array, [PURPLE if x == i else YELLOW if x == 0 else BLUE if x > i else ORANGE for x in range(len(array))])
        time.sleep(timeTick/4)
        drawArray(array, [BLUE if x >= i else ORANGE for x in range(len(array))])
        time.sleep(timeTick/4)
        heapify(array, i, 0, drawArray, timeTick,i-1)
        time.sleep(timeTick/4)
        drawArray(array, [BLUE if x >= i else ORANGE for x in range(len(array))])
        time.sleep(timeTick/4)

    drawArray(array, [BLUE for x in range(len(array))])