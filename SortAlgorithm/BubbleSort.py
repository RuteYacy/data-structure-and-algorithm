def bubbleSort(customLL):
    for i in range(len(customLL)-1):
        for j in range(len(customLL)-i-1):
            if customLL[j] > customLL[j+1]:
                customLL[j], customLL[j+1] = customLL[j+1], customLL[j]
    print(customLL)
    
def selectionSort(customLL):
    for i in range(len(customLL)):
        min_index = i
        for j in range(i+1, len(customLL)):
            if customLL[min_index] > customLL[j]:
                min_index = j
        customLL[j], customLL[min_index] = customLL[min_index], customLL[j]
    print(customLL)
    
