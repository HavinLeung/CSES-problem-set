from sys import stdin

def main():
    n = int(input())
    weights = list(map(int, stdin.readline().split()))
    ans = [10**9]
    def dfs(i, running):
        if i >= n:
            ans[0] = min(abs(running), ans[0])
            return
        dfs(i+1, running + weights[i])
        dfs(i+1, running - weights[i])
    dfs(0,0)
    print(ans[0])


main()
