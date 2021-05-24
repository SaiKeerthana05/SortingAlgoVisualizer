### INSERTION SORT ###

import time
from Sorting_Visualizer.colors import *


def insertion_sort(array, drawArray, timeTick):
    for i in range(len(array)):
        temp = array[i]
        k = i
        drawArray(array, [BLUE if x < i else DARK_ORANGE if x == i else ORANGE for x in range(len(array))])
        time.sleep(timeTick/3)
        while k > 0 and temp < array[k - 1]:
            array[k],array[k-1] = array[k - 1],array[k]
            drawArray(array, [DARK_ORANGE if x == k-1 else BLUE if x <= i else ORANGE for x in range(len(array))])
            time.sleep(timeTick/3)
            k -= 1
        array[k] = temp
        drawArray(array, [BLUE if x <= i else ORANGE for x in range(len(array))])
        time.sleep(timeTick/3)

    drawArray(array, [BLUE for x in range(len(array))])