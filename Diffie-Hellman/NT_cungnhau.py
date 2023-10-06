def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_phi(n):
    phi = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            phi += 1
    return phi

def coprime_numbers_with_n(n):
    coprimes = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def is_primitive_root(a, n, phi_n):
    factors = prime_factors(phi_n)
    for p in factors:
        if pow(a, phi_n // p, n) == 1:
            return False
    return True

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return set(factors)

def select_primitive_root(primitive_roots):
    while True:
        for i, root in enumerate(primitive_roots):
            print(f"{i + 1}. {root}")
        
        choice = input("Chọn một căn nguyên thủy (1, 2, ...) hoặc nhấn Enter để thoát: ")
        if choice == "":
            return None  # Người dùng không chọn gì, trả về None
        try:
            index = int(choice) - 1
            if 0 <= index < len(primitive_roots):
                return primitive_roots[index]  # Trả về căn nguyên thủy được chọn
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")



# Example usage:
n = 29  # Thay đổi giá trị của n tại đây
phi_n = euler_phi(n)

print(f"Số các số nguyên tố cùng nhau với {n} là {phi_n}:")
coprimes = coprime_numbers_with_n(n)
print(coprimes)

primitive_roots = []
for a in coprimes:
    if is_primitive_root(a, n, phi_n):
        primitive_roots.append(a)
        
print(f"Các căn nguyên thủy của {n} là:")
print(primitive_roots)
        
selected_root = select_primitive_root(primitive_roots)
if selected_root is not None:
    print(f"Bạn đã chọn căn nguyên thủy: {selected_root}")
else:
    print("Bạn đã thoát chương trình.")

