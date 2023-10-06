import random

max_PrimLength = 1000000000000

# Eculid mở rộng (nghịch đảo modulus)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Tìm UCLN
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ktra SNT
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

# Random 1 SNT
def generateRandomPrim():
    while True:
        ranPrime = random.randint(0, max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime

# Tính toán d (e^-1 mod phi)
def calculate_d(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:  # Kiểm tra e và phi có nguyên tố cùng nhau hay không
        raise ValueError("e is not coprime to phi")
    # d = e^-1 mod phi => d = x % phi (x là hê số bezout của ptr eculid mở rộng)
    d = x % phi
    if d < 0:
        d += phi
    return d

# Hàm tạo khóa RSA: công khai và bí mật
def generate_keyPairs():
    p = generateRandomPrim() # random SNT
    q = generateRandomPrim()
    # p = 73
    # q = 151
    print ("p = ", p, " q = ", q)
    
    # Tính n
    n = p * q
    print("n = ", n)
    # Tính phi 
    phi = (p - 1) * (q - 1)
    print("phi = ", phi)
    
    # e = 11 
    e = random.randint(1, phi) 
    while gcd(e, phi) != 1:
       e = random.randint(1, phi)
       
    print(f"UCLN của {e} và {phi} là: ", gcd(e, phi))
       
    d = calculate_d(e, phi)

    print("e =", e ,"\n", "d =", d) 

    return ((e, n), (d, n))

def decrypt(ctext, private_key):
    try:
        key, n = private_key
        text = [chr(pow(char, key, n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

def encrypt(text, public_key):
    key, n = public_key
    
    ctext = [pow(ord(char), key, n) for char in text]
    return ctext

if __name__ == '__main__':
    public_key, private_key = generate_keyPairs()
    print("Public: ", public_key)
    print("Private: ", private_key)
    
    text = input("Nhập text: ")
    
    
    ctext = encrypt(text, public_key)
    print("encrypted  =", ctext)
    plaintext = decrypt(ctext, private_key)
    print("decrypted =", plaintext)