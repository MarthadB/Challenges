#Sequential Sort
def sequentialSortA(array,size): #Ascending Order

    for i in range(size):
        min = i

        for j in range(i + 1,size):
            if array[j] < array[min]: 
                min = j
        (array[i], array[min]) = (array[min], array[i]) 

Array = [4,99,-54,34,-12]
size = len(Array)
sequentialSortA(Array,size)
print('Ascending Order:')
print(Array)

def sequentialSortD(array,size): #Descending Order

    for i in range(size):
        max = i

        for j in range(i + 1,size):
            if array[j] > array[max]:
                max = j
        (array[i], array[max]) = (array[max], array[i])

sequentialSortD(Array,size)
print('Descending Order:')
print(Array)



