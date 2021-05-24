### SELECTION SORT ###

import time
from Sorting_Visualizer.colors import *


def selection_sort(array, drawArray, timeTick):
    for i in range(len(array) - 1):
        minimum = i
        for k in range(i + 1, len(array)):
            drawArray(array, [DARK_ORANGE if x == k else BLUE if x < i else LIGHT_GREEN if x == minimum else ORANGE for x in range(len(array))])
            time.sleep(timeTick/3)
            if array[k] < array[minimum]:
                minimum = k
                drawArray(array, [LIGHT_GREEN if x == minimum else BLUE if x < i else ORANGE for x in range(len(array))])
                time.sleep(timeTick/3)
            else:
                drawArray(array, [LIGHT_GREEN if x == minimum else BLUE if x < i else ORANGE for x in range(len(array))])
                time.sleep(timeTick/3)

        array[minimum],array[i] = array[i], array[minimum]
        time.sleep(timeTick/3)

    drawArray(array, [BLUE for x in range(len(array))])