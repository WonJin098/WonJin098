arr = []
N = int(input("N: "))

def p_min_map(board):
    for row in board:
        print(' '.join(row))

def f_min_map(arr):
    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == '0':
                count = 0
                for x in range(max(0, i - 1), min(i + 2, rows)):
                    for y in range(max(0, j - 1), min(j + 2, cols)):
                        if arr[x][y] == '1':
                            count += 1
                arr[i][j] = str(count)

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == '1':
                arr[i][j] = '*'

    p_min_map(arr)

print("0 과 1 중 하나만 입력해 주세요 : ")
for _ in range(N):
    row = input().split()
    arr.append(row)

f_min_map(arr)
