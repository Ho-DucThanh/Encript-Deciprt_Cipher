def generate_key(length):
    """Tạo khóa ngẫu nhiên với độ dài 'length' (số lượng bit)"""
    key = ""
    for _ in range(length):
        key += str(random.randint(0, 1))
    return key

def text_to_binary(text):
    """Chuyển đổi văn bản thành chuỗi bit"""
    binary_text = ""
    for char in text:
        binary_char = bin(ord(char))[2:]  # Chuyển đổi ký tự thành chuỗi bit binary
        binary_text += binary_char.zfill(8)  # Đảm bảo rằng mỗi ký tự có độ dài 8 bit
    return binary_text

def binary_to_text(binary_text):
    """Chuyển đổi chuỗi bit thành văn bản"""
    text = ""
    for i in range(0, len(binary_text), 8):
        binary_char = binary_text[i:i+8]
        char = chr(int(binary_char, 2))  # Chuyển đổi chuỗi bit thành ký tự
        text += char
    return text

def encrypt(plaintext, key):
    """Mã hóa thông điệp sử dụng khóa và trả về bản mã dưới dạng chuỗi bit"""
    if len(plaintext) != len(key):
        raise ValueError("Độ dài của khóa phải bằng độ dài của thông điệp")

    ciphertext = ""
    for i in range(len(plaintext)):
        xor_result = int(plaintext[i]) ^ int(key[i])  # Phép XOR giữa các bit
        ciphertext += str(xor_result)
    return ciphertext

def main():
    plaintext = input("Nhập vào bản rõ: ")
    plaintext_binary = text_to_binary(plaintext)

    key = generate_key(len(plaintext_binary))
    ciphertext_binary = encrypt(plaintext_binary, key)

    print(f"Bản rõ:      {plaintext}")
    print(f"Bản rõ (bit): {plaintext_binary}")
    print(f"Khóa:        {key}")
    print(f"Bản mã:     {ciphertext_binary}")

if __name__ == "__main__":
    import random
    main()