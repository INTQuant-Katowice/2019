number_one = 1  # int
number_two = 2.0  # float

string = 'Hello World!'

empty_list = []
my_list = [1, 5.0, 'bla bla']
my_list.append([5, 6, 32.90373])

my_tuple = (4, 5, 6)  # I'm a tuple and I'm immutable.


empty_dictionary = {}
my_dict = {'key': 'value',
           'name': 'Alice',
           'eyes colour': 'blue',
           'height': 175,
           'favourite numbers': [3,7]}

my_dict['name']  # will print 'Alice'

for key in my_dict:
    print(my_dict[key])

for item in my_list:
    print(item * 2)

i=0
while i<5:
    print(i)
    i += 1

for i in range(5):
    print(i)

for i in range(len(my_list)):
    print(my_list[i])

for i in range(22):
    if i%7 == 0 and i%3 == 0:
        print(i, 'divisible by 7 and 3')
    elif i%7 == 0:
        print(i, 'divisible by 7')
    elif i%3 == 0:  # additional if
        print(i, 'divisible by 3')
    else:
        print(i, 'indivisible by 3 or 7')
#####################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = np.linspace(0.25, 80, num=100)
B = np.linspace(0.20, 90, num=100)
C = np.linspace(0.27, 100, num=100)

df = pd.DataFrame({'A': A,
                   'B': B,
                   'C': C})

mean = df.mean(axis=1)
std = df.std(axis=1)
var = df.var(axis=1)

df['MEAN'] = mean
# df.drop('MEAN', axis=1) #if you want to delete a column

df['STD_DEV'] = std
df['VAR'] = var


bigger_than_ten = df[df.A > 10.0]  # examples of filtering
even_index = df[df.index%2 == 0]

# plt.figure()
plt.plot(df.MEAN)
#
plt.scatter(df.index, df.MEAN)
plt.scatter(df.index, df.STD_DEV)
plt.scatter(df.index, df.VAR)
plt.ylabel('value')
plt.xlabel('index')
plt.title('my plot')
plt.legend()
plt.show()

df.to_csv(r'path_to_the_file.csv',
             header=True)
frame = pd.read_csv(r'path_to_the_file.csv')
#####################################################################################

random_array = np.random.uniform(-2, 2, (3, 100))
normal_array = np.random.normal(size=(3, 100))

