import random


def test():
    komputer_point = 0
    gemer_point = 0
    while True:
        input("Coś")
        x = random.randint(1, 6) + random.randint(1, 6)
        y = random.randint(1, 6) + random.randint(1, 6)
        komputer_point += y
        gemer_point += x
        print(f"{komputer_point}, {gemer_point}")
        if komputer_point > 2001 or gemer_point > 2001:
            break


test()