import random
from math import gcd

def is_prime(num):
    # Проверка числа на простоту
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_number(bit_length):
    # Генерация случайного простого числа заданной длины (в битах)
    num = random.getrandbits(bit_length)
    while not is_prime(num):
        num = random.getrandbits(bit_length)
    return num

def euler_function(p, q):
    # Вычисление значения функции Эйлера от числа n
    return (p - 1) * (q - 1)

def generate_keypair():
    # Генерация открытого и закрытого ключей
    bit_length = 32  # Длина простых чисел в битах
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)
    n = p * q
    fi = euler_function(p, q)

    e = random.randint(2, fi)
    while gcd(e, fi) != 1:
        e = random.randint(2, fi)

    d = pow(e, -1, fi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Генерация ключей
public_key, private_key = generate_keypair()

# Шифрование и расшифровка сообщения
message = "Hello world"
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

# Вывод результатов
print("Открытый ключ (n, e):", public_key)
print("Закрытый ключ (n, d):", private_key)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
