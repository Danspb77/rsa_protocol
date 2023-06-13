import random

from math import gcd as bltin_gcd

# проверка на взаимную простоту
def coprime2(a, b):
    return bltin_gcd(a, b) == 1

# проверка на  простоту
def is_prime_num(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

# generate rand numbers
def simp_rand_num():
    num=random.randint(1,32)
    while is_prime_num(num)!=True:
        num=random.randint(1,32)
    return num


def eiler_function(n,q):
    return (n-1)*(q-1)

#  generate e
def e_generate(fi):
    e=random.randint(1,fi)
    while not coprime2(e,fi):
        e=random.randint(1,fi)
    return e

# def d_generate(e,fi):
#     d=random.randint(2,e)
#     while not ((d*e)%fi==1):
#         d=random.randint(2,q)
#     return d 


p=(simp_rand_num())
q=(simp_rand_num())
fi=eiler_function(p,q)
e=e_generate(fi)
print(e)
# d=d_generate(open_exp,fi)
# print(d)
print(fi) 


# print((open_exp*d)%fi)

print(p,q)


