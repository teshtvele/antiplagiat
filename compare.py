import re
import argparse
import pickle
import sys
import ast


def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

def score(path1, path2):

    with open(path1, 'r') as f:
        text1 = f.read()

    with open(path2, 'r') as f:
        text2 = f.read()

    dist = levenstein(text1, text2)
    result = (len(text1) - dist) / len(text2)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str)
    args = parser.parse_args()

    with open(args.input, 'r') as pathes:
        for path in pathes.readlines():
            file1, file2 = path.split()
            result = score(file1, file2)
            with open(args.output, 'a+') as outFile:
                outFile.write(str(score) + '\n')