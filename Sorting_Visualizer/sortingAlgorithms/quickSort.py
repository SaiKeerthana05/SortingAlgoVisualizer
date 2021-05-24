### QUICK SORT ###

import time

from Sorting_Visualizer.colors import *


def partition(array, pivots, start, end, drawArray, timeTick):
    drawArray(array, [YELLOW if x == start else BLUE if x in pivots else ORANGE for x in range(len(array))])
    time.sleep(timeTick/4)
    i = start + 1
    pivot = array[start]

    for j in range(start + 1, end + 1):
        if array[j] < pivot:
            if j!=i:
                drawArray(array, [
                YELLOW if x == start else BLUE if x in pivots else LIGHT_GREEN if x < i and x > start else RED if x == j else PURPLE if x >= i and x < j else ORANGE
                for x in range(len(array))])
                time.sleep(timeTick/3)
            array[i], array[j] = array[j], array[i]
            if j!=i:
                    drawArray(array, [YELLOW if x == start else BLUE if x in pivots else LIGHT_GREEN if x < i and x > start else RED if x == i else PURPLE if x > i and x <= j else ORANGE for x in range(len(array))])
                    time.sleep(timeTick/3)
            drawArray(array, [YELLOW if x == start else BLUE if x in pivots else LIGHT_GREEN if x <= i and x > start else PURPLE if x > i and x <= j else ORANGE for x in range(len(array))])
            time.sleep(timeTick/3)
            i += 1
        else:
            drawArray(array, [YELLOW if x == start else BLUE if x in pivots else LIGHT_GREEN if x < i and x > start else PURPLE if x >= i and x <= j else ORANGE for x in range(len(array))])
            time.sleep(timeTick/3)


    array[start], array[i - 1] = array[i - 1], array[start]
    drawArray(array, [BLUE if x in pivots else YELLOW if x == i - 1 else LIGHT_GREEN if x < i - 1 and x >= start else PURPLE if x >= i and x <= j else ORANGE for x in range(len(array))])
    time.sleep(timeTick/3)
    pivots.append(i - 1)
    drawArray(array, [BLUE if x in pivots else ORANGE for x in range(len(array))])
    time.sleep(timeTick/3)
    return i - 1


def quick_sort(array, pivots, start, end, drawArray, timeTick):
    if start < end:
        pivot_position = partition(array, pivots, start, end, drawArray, timeTick)
        quick_sort(array, pivots, start, pivot_position - 1, drawArray, timeTick)
        drawArray(array, [BLUE if x in pivots else ORANGE for x in range(len(array))])
        time.sleep(timeTick/4)
        quick_sort(array, pivots, pivot_position + 1, end, drawArray, timeTick)
        drawArray(array, [BLUE if x in pivots else ORANGE for x in range(len(array))])
        time.sleep(timeTick/4)
    else :
        if start == end:
            pivots.append(start)
            drawArray(array, [BLUE if x in pivots else ORANGE for x in range(len(array))])
            time.sleep(timeTick/4)

    drawArray(array, [BLUE for x in range(len(array))])
