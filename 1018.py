N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        index_0 = 0
        index_1 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0