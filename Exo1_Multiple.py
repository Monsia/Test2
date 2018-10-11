def multiple_3_5 (n):
    somme = 0

    for i in range (n):
        if i % 3 == 0 or i % 5 == 0:
            somme += i
    return somme

print(multiple_3_5(1000))

