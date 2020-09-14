def steps(number):
    n = number
    i = 0

    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        i = i + 1

    if n == 1 :
        # print("You reached 1 in", i, "steps")
        return i
