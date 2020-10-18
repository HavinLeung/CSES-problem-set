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
    N = 8
    board = read_matrix(N, lambda s: list(map(lambda x: True if x == '.' else False, s)))
    used_positions = set()
    num_ways = 0
    def can_use(row, col):
        if not board[row][col]:
            return False
        for used_row, used_col in used_positions:
            if row == used_row or col == used_col:
                return False
            if abs(row - used_row) == abs(col - used_col):
                return False
        return True
    def dfs(row=0):
        nonlocal num_ways
        if row >= N:
            return
        for col in range(N):
            if can_use(row, col):
                if row == N - 1:
                    num_ways += 1
                used_positions.add((row,col))
                dfs(row+1)
                used_positions.remove((row,col))

    dfs()
    print(num_ways)

main()
