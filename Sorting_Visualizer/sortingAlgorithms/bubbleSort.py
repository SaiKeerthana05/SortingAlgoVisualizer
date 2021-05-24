### BUBBLE SORT ###

import time
from Sorting_Visualizer.colors import *


def bubble_sort(array, drawArray, timeTick):
    size = len(array)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                drawArray(array, [RED if x == j or x == j + 1 else BLUE if x >= size-i  else ORANGE for x in range(len(array))])
                time.sleep(timeTick/3)
                array[j], array[j + 1] = array[j + 1], array[j]
                drawArray(array, [LIGHT_GREEN if x == j or x == j + 1 else BLUE if x >= size-i else ORANGE for x in range(len(array))])
                time.sleep(timeTick/3)
            else:
                drawArray(array, [LIGHT_GREEN if x == j or x == j + 1 else BLUE if x >= size-i else ORANGE for x in range(len(array))])
                time.sleep(timeTick/3)

    drawArray(array, [BLUE for x in range(len(array))])
