import numpy as np
import random
import pandas as pd
distance = set()
while len(distance)< 100:
  random_float = random.uniform(0,15)
  distance.add(random_float)
distance_list = list(distance)

size = []
for i in range(100):
  random_int = random.randint(45,150)
  size.append(random_int)

distance_value = []
for i in distance_list:
  distance_value.append(1 / i)

dataset = []
for i in range(0,100):
  dataset.append([size[i], distance_list[i]])

for i in range(0,100):
  dataset[i].append(size[i]*distance_value[i])


def Sort(dataset):
  dataset.sort(key = lambda x: x[2])
  return dataset            


new_dataset = Sort(dataset)
#print("sorted dataset: ")
#for lm in new_dataset:
#  text=""
#  for sub_lm in lm:
#    text += str(sub_lm) + "\t\t"  
#  print(text)  



def changedDataset(new_dataset):
  value = 3000
  for lm in range(0, len(new_dataset)-1, 1):
    new_dataset[lm][2] = value
    value += 100   
  return new_dataset

print("sorted final dataset: ")
for lm in changedDataset(new_dataset):
  text =""
  for sub_lm in lm:
    text += str(sub_lm) + "\t\t"
  print(text)
  
numpy_dataset = np.array(new_dataset)
print(numpy_dataset)
df = pd.DataFrame(numpy_dataset)
df.columns = ["m2", "distance to sea", "rent as dollar"]

df.to_csv('numpy_dataset.csv', index=False)
  

  