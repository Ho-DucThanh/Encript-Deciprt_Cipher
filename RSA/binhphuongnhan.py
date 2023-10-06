def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  
    while exponent > 0:
        # Nếu bit cuối của exponent là 1, nhân result với base và lấy modulo
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # Bình phương base và giảm exponent đi một nửa
        base = (base * base) % modulus
        exponent = exponent // 2
    
    return result

# Tính 72^11 mod 11023
result = modular_exponentiation(112, 7, 323)
print("Result = ", result)
