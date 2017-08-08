def fak(n):
    if n > 1:
        return n * fak(n-1)
    else:
        return 1

print(fak(5))