def f(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    elif n == 2:
        return [0,1,1]
    else:
        sequence = [0,1,1]
        for i in range(3,n,):
            next_value = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_value)
        return sequence
    
n = int(input())
print(f(n))
