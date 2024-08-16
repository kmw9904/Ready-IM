N = int(input())
stack = []
for i in range(1, N + 1):
    clap = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if clap > 0:
        stack.append('-'*clap)
    else:
        stack.append(i)
print(*stack, end=' ')
