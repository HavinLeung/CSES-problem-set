from sys import stdin
from pprint import pprint

def read_multiple(from_str_constructor, delimiter=''):
    return list(map(from_str_constructor, stdin.readline().strip().split(sep=delimiter)))

def read_single(from_str_constructor):
    return from_str_constructor(stdin.readline().strip())

def read_matrix(num_rows , str_to_row_constructor):
    l = []
    for _ in range(num_rows):
        l.append(str_to_row_constructor(stdin.readline().strip()))
    return l

def main():
    n = read_single(int)
   
main()
