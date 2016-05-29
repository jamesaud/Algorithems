from collections import defaultdict
from itertools import islice

def answer(LoN):
    indexLimits = calculateStartAndEndIndexes(LoN)
    startIndex, endIndex = indexLimits[0], indexLimits[1]
    #Heights with index positions
    #{10 : [0,4,5]}
    heights_to_index = defaultdict(list)
    for i in range(startIndex, endIndex+1):
        height = LoN[i]
        heights_to_index[height].append(i)

    index_list = [heights_to_index[height] for height in reversed(sorted(heights_to_index))]
    index_groups = calculateIndexDictionary(index_list)

    waterfilled_area = 0
    while index_groups.get(startIndex, None) and index_groups.get(startIndex) != startIndex:
        endIndex = index_groups.get(startIndex)
        waterfilled_area += calculateBox(LoN, startIndex, endIndex)
        startIndex = endIndex
    return waterfilled_area

def calculateBox(LoN, startIndex, endIndex):
    width = endIndex - startIndex - 1
    filled = 0
    if LoN[startIndex] < LoN[endIndex]:
        smaller = LoN[startIndex]
    else:
        smaller = LoN[endIndex]
    startIndex += 1
    while startIndex < endIndex:
        filled += LoN[startIndex]
        startIndex += 1
    area = smaller * width - filled
    return area

#Takes in a list of indexes and returns a dictionary, connected "peak to peak"
def calculateIndexDictionary(index_list):
    index_paths = {}
    min, max = index_list[0][0], index_list[0][-1]
    index_paths[min] = max
    for indexes in index_list:
        low, high = indexes[0], indexes[-1]
        if low < min:
            index_paths[low] = min
            min = low
        if high > max:
            index_paths[max] = high
            max = high
  #  print(index_paths)
    return index_paths

#Finds the first peak on the left and right sides and returns the index positions
#LoN -> (left, right)
def calculateStartAndEndIndexes(LoN):
    length = len(LoN)
    indexes = [0, len(LoN)-1]
    for i in range(length-2):
        if LoN[i] > LoN[i+1]:
            indexes[0] = i
            break
    for i in range(length-1, 1, -1):
        if LoN[i - 1] < LoN[i]:
            indexes[1] = i
            break
    return indexes


test = [1, 10, 4, 6, 5, 2, 3, 2, 4]
print(answer(test))
