T = int(input())

for tc in range(1, T + 1):
    N = input()
    lst = []
    for l in N:
        lst.append(int(l))
    n = len(lst)
    arr = [0] * n
    cnt = 0

    for i in range(n):

        if lst[i] != arr[i]:

            if lst[i] == 1:
                for j in range(i, n):
                    arr[j] = 1
                cnt += 1
                if lst == arr:
                    print(f'#{tc} {cnt}')
                    break
            elif lst[i] == 0:
                for j in range(i, n):
                    arr[j] = 0
                cnt += 1
                if lst == arr:
                    print(f'#{tc} {cnt}')
                    break
