def toplam(n):
    if n==0:
        return 0
    else:
        return n+toplam(n-1)
