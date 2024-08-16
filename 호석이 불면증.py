T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

    for j in range(1, 100):

        result = N * j
        arr = str(result)

        for k in arr:
            lst[k] = 1

        if sum(lst.values()) == 10:
            print(f'#{tc} {result}')
            break
