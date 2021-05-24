### MERGE SORT ###

import time

from Sorting_Visualizer.colors import *


def merge(array, start, mid, end, drawArray, timeTick):
    drawArray(array, [PURPLE if x < start else ORANGE for x in range(len(array))])
    time.sleep(timeTick/2)
    p = start
    q = mid + 1
    tempArray = []
    cur = start
    for i in range(start, end + 1):
        if p > mid:
            tempArray.append(array[q])
            q += 1
            cur += 1
        elif q > end:
            tempArray.append(array[p])
            p += 1
            cur += 1
        elif array[p] < array[q]:
            drawArray(array,
                      [LIGHT_GREEN if x == p or x == q else PURPLE if x < start else ORANGE for x in range(len(array))])
            time.sleep(timeTick/2)
            tempArray.append(array[p])
            p += 1
            cur += 1
        else:
            drawArray(array, [RED if x == p or x == q else PURPLE if x < start else ORANGE for x in range(len(array))])
            time.sleep(timeTick/2)
            tempArray.append(array[q])
            k = q - 1
            save = array[q]
            while k >= cur:
                array[k + 1] = array[k]
                k -= 1
            array[cur] = save
            drawArray(array, [PURPLE if x < cur else LIGHT_GREEN if x == cur or x == q else ORANGE for x in range(len(array))])
            time.sleep(timeTick/2)
            p += 1
            q += 1
            mid+=1
            cur+=1

    for p in range(len(tempArray)):
        array[start] = tempArray[p]
        start += 1


def merge_sort(array, start, end, drawArray, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(array, start, mid, drawArray, timeTick)
        merge_sort(array, mid + 1, end, drawArray, timeTick)

        merge(array, start, mid, end, drawArray, timeTick)

        drawArray(array, [PURPLE if x <= end else ORANGE for x in range(len(array))])
        time.sleep(timeTick/2)

    drawArray(array, [BLUE for x in range(len(array))])
