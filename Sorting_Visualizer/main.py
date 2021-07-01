import tkinter

# tkinter --> GUI Library of Python
from tkinter import *

# For creating the random arrays
import random
from tkinter.ttk import Combobox

from Sorting_Visualizer.colors import *

from Sorting_Visualizer.sortingAlgorithms.bubbleSort import bubble_sort
from Sorting_Visualizer.sortingAlgorithms.heapSort import heap_sort
from Sorting_Visualizer.sortingAlgorithms.insertionSort import insertion_sort
from Sorting_Visualizer.sortingAlgorithms.mergeSort import merge_sort
from Sorting_Visualizer.sortingAlgorithms.quickSort import quick_sort
from Sorting_Visualizer.sortingAlgorithms.selectionSort import selection_sort

# Creating a base window
baseWindow = Tk()
baseWindow.title("Sorting Algorithm Visualizer")
baseWindow.maxsize(1600,800)
baseWindow.geometry("900x800+160+50")
baseWindow.config(bg = LIGHT_PURPLE)

algorithmName = StringVar()
# algoList to store different sorting algorithms
algorithmList = ['Selection Sort','Insertion Sort','Bubble Sort','Merge Sort','Quick Sort','Heap Sort']

speedLevel = StringVar()
# speedList is to select the speed for visualization
speedList = ['Fast','Medium','Slow']

# A list to store the randomly generated elements of an array
array = []

# Function to draw randomly generated list array[] on the canvas as vertical bars
def drawArray(array, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(array) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(array) for i in array]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i],outline=colorArray[i])

    baseWindow.update_idletasks()

# Function to generate an array with random values when the generate button is clicked
def generate():
    global array, pivots

    array = []
    pivots = []
    n = sizeScale.get()
    for i in range(0, n):
        random_value = random.randint(1, 150)
        array.append(random_value)

    drawArray(array, [ORANGE for x in range(len(array))])


# To set speed of visualization
def setSpeed():
    if speed_menu.get() == 'Slow':
        return 1.4
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.002

# Function to start sorting according to the selected algorithm
def sort():
    global array
    timeTick = setSpeed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(array, drawArray, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(array, drawArray, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(array, drawArray, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(array, 0, len(array) - 1, drawArray, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(array, pivots, 0, len(array) - 1, drawArray, timeTick)
    else:
        heap_sort(array, drawArray, timeTick)

### FOR USER INTERFACE ###
UI_Frame = Frame(baseWindow, width=1000,height=500,bg=WHITE)
UI_Frame.grid(row=0,column=0,padx=10,pady=5)

# To create dropdown list to select sorting algorithm
dropDownList_algo = Label(UI_Frame,text="Algorithm: ",bg=WHITE)
dropDownList_algo.grid(row=0,column=0,padx=10,pady=5,sticky=W)
algo_menu = Combobox(UI_Frame,textvariable=algorithmName,values=algorithmList)
algo_menu.grid(row=0,column=1,padx=5,pady=5)
algo_menu.current(0)

# To create dropdown list to select speed of visualisation
dropDownList_speed = Label(UI_Frame,text="Speed: ",bg=WHITE)
dropDownList_speed.grid(row=1,column=0,padx=10,pady=5,sticky=W)
speed_menu = Combobox(UI_Frame,textvariable=speedLevel,values=speedList)
speed_menu.grid(row=1,column=1,padx=5,pady=5)
speed_menu.current(0)

# Scale to select the size of the array
size = Label(UI_Frame,text="Select array size: ",bg=WHITE)
size.grid(row=2,column=0,padx=10,pady=5,sticky=W)
arraySize = IntVar()
sizeScale = Scale(UI_Frame, variable=arraySize,from_=1, to=100,orient=HORIZONTAL)
sizeScale.grid(row=2,column=1,padx=5,pady=5)

# Button to start sorting
button_sort = Button(UI_Frame,text="Sort",command=sort,bg=LIGHT_GRAY)
button_sort.grid(row=3,column=1,padx=5,pady=5)

# Button to generate an array
button_generate = Button(UI_Frame,text="Generate array",command=generate,bg=LIGHT_GRAY)
button_generate.grid(row=3,column=0,padx=5,pady=5)

# To reconfigure widgets
baseWindow.rowconfigure(0,weight=1)
baseWindow.rowconfigure(1,weight=1)
baseWindow.rowconfigure(2,weight=1)
baseWindow.rowconfigure(3,weight=1)

baseWindow.columnconfigure(0,weight=1)
baseWindow.columnconfigure(1,weight=1)
baseWindow.columnconfigure(2,weight=1)
baseWindow.columnconfigure(3,weight=1)

# Canvas to draw our array
canvas = Canvas(baseWindow,width=1000,height=420,bg=WHITE)
canvas.grid(row=1,column=0,padx=10,pady=5,sticky='S')


baseWindow.mainloop()
