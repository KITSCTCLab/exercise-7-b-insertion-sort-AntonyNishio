from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  for step in range(1, len(array)):
        key = array[step]
        j = step - 1
       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
    
insertionSort(data)
print(data)
