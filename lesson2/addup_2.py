def addup(n):
    a = 0
    for i in range(1, n):
        a = a + i
    return a

print(addup(100))