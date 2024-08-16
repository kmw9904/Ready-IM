T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    mx_result = 0

    if M > N:

        for i in range(M - N + 1):
            result = 0
            for j in range(N):

                result += Ai[j] * Bi[i + j]
            if mx_result < result:
                mx_result = result
    else:

        for i in range(N - M + 1):
            result = 0
            for j in range(M):
                result += Ai[j+i] * Bi[j]
            if mx_result < result:
                mx_result = result

    print(f'#{tc} {mx_result}')