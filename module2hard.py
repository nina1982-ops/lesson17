import random


def multipicity(rand_num):
    num_ = ""
    ff = 0
    for i in range(1, n):
        if i > n / 2:
            break
        for k in range(i + 1, n):
            if n % (i + k) == 0:
                num_ += str(i) + str(k)
                print(i, ' ', k)
                ff += 1
    print(ff)
    return num_


n = random.randint(3, 20)
print(n)
password = multipicity(n)
print(password)
