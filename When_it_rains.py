from collections import defaultdict
from itertools import islice

#Visualizing the problem as a vertical Bar Graph, vertical bars are connected "peak to peak"/
#This forms horizontal rectangles between the peaks, in which area can be calculated
def answer(LoN):
    #Returns a list of two indexes, starting and ending from the first and last peaks
    indexLimits = calculateStartAndEndIndexes(LoN)
    startIndex, endIndex = indexLimits[0], indexLimits[1]

    #Height with matching List of Index Positions
    heights_to_index = defaultdict(list) #{height : [index,index,...]}
    for i in range(startIndex, endIndex+1):
        heights_to_index[LoN[i]].append(i)

   #List of [List of indexes], sorted in descending order of height
    index_list = [heights_to_index[height] for height in reversed(sorted(heights_to_index))]

    #Get dictionary of indexes from "peak to peak"
    index_peaks = calculateIndexDictionary(index_list)

    #Loop through all the peaks and compute areas
    #Go from peak to peak by looping: key = key[value]
    #Second while loop condition prevents a side effect of the last key looping to itself
    waterfilled_area = 0
    while index_peaks.get(startIndex, None) and index_peaks.get(startIndex) != startIndex:
        endIndex = index_peaks.get(startIndex)
        waterfilled_area += calculateBox(LoN, startIndex, endIndex)
        startIndex = endIndex
    return waterfilled_area

#Calculates the amount of "filled water" in a box
#Think of the visual representation as a bar graph, where the left and right sides are the the tallest bars/
#You can form a horizontal rectangle, and calculate the unfilled area
#LoN, start, end -> number
def calculateBox(LoN, startIndex, endIndex):
    width = endIndex - startIndex - 1
    filled = 0

    #Height of rectangle is the shorter of the right and left sides
    if LoN[startIndex] < LoN[endIndex]:
        smaller = LoN[startIndex]
    else:
        smaller = LoN[endIndex]

    #Middle of the left and right is the filled amount
    startIndex += 1
    while startIndex < endIndex:
        filled += LoN[startIndex]
        startIndex += 1
    #UnfilledArea = Area[Smaller*Width] - FilledArea
    return smaller * width - filled

#Takes in a list of list of indexes sorted by largest heights to smallest, and returns a dictionary of indexes connected "peak to peak"
#ListOfLists -> dictionary{number : number}
def calculateIndexDictionary(index_list):
    index_paths = {}
    #Set initial index "peak" paths. The last index could link to itself, a side effect. Still computers to an area of 0
    min, max = index_list[0][0], index_list[0][-1]
    index_paths[min] = max

    for indexes in index_list:
        low, high = indexes[0], indexes[-1]
        #Only set a peak path if it is not already encapsulated by a larger peak path
        if low < min:
            index_paths[low] = min
            min = low
        if high > max:
            index_paths[max] = high
            max = high
    return index_paths

#Finds the first peak on the left and right sides and returns the index positions
#The first peaks are when the visualization of vertical bars change from increasing to decreasing
#LoN -> (startIndex, endIndex)
def calculateStartAndEndIndexes(LoN):
    length = len(LoN)
    #Default is first index to last
    indexes = [0, length-1]
    #Go from left to right
    for i in range(length-2):
        if LoN[i] > LoN[i+1]:
            indexes[0] = i
            break
    #Go from Right to Left
    for i in range(length-1, 1, -1):
        if LoN[i - 1] < LoN[i]:
            indexes[1] = i
            break
    return indexes
test = [1, 10, 4, 6, 5, 2, 3, 2, 4]
print(answer(test))
