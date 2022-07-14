#!/usr/bin/env python3


array_input = []
print('Enter successively four inputs sepatated by commas:')
for x in range(4):
    array_input.append([y for y in input().split()])

def create_arrays(array):
    for elem in array:
        rows, column = elem[0].split(',')[0], elem[0].split(',')[1]
        a = [y+1 for y in range(int(column)*int(rows))]
        chunk_size = int(column)
        chunked_list = [a[i:i+chunk_size] for i in range(0, len(a), chunk_size)]
        print(chunked_list)

if __name__ == "__main__": create_arrays(array_input)