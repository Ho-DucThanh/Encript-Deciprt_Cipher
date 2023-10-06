import random
import string

def generate_random_key(length):
    # Tạo một chuỗi ngẫu nhiên bằng cách kết hợp các ký tự trong khoảng a-z
    key = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    # random.choice() dùng để chọn một phần tử ngẫu nhiên từ một dãy hoặc chuỗi
    # string.ascii_lowercase là một chuỗi chứa tất cả các chữ cái thường trong bảng chữ cái tiếng Anh từ 'a' đến 'z'
    # join dùng để nối các chuỗi con lại với nhau
    return key

def vernam_decrypt(cipher_text, key):
    cipher_text = cipher_text.lower()  # Chuyển về chữ in thường
    key = key.lower()
    cipher_text = cipher_text.replace(" ", "")
    key = key.replace(" ", "")

    plain_text = ""

    for i in range(len(cipher_text)):
        k1 = ord(cipher_text[i]) - 97
        k2 = ord(key[i]) - 97
        print(k1, k2)
        s = chr((((k1 - k2) + 26) % 26) + 97)
        plain_text += s

    return plain_text  # Trả về văn bản đã giải mã


def vernam_encrypt(plain_text, key):
    plain_text = plain_text.replace(" ", "")
    key = key.replace(" ", "")
    plain_text = plain_text.lower()
    key = key.lower()

    if len(plain_text) != len(key):
        return "Lengths are different"

    cipher_text = ""

    for i in range(len(plain_text)):
        k1 = ord(plain_text[i]) - 97
        k2 = ord(key[i]) - 97
        s = chr((k1 + k2) % 26 + 97)
        cipher_text += s

    return cipher_text  # Trả về văn bản đã mã hóa


def main():
    plain_text = input("Nhập plainText: ")
    
    while True:
        key = input("Nhập key: ")
        if len(key) < len(plain_text):
            print("Key không hợp lệ! Vui lòng nhập lại")
            continue
        break

    # key_length = len(plain_text)
    # random_key = generate_random_key(key_length)
    # print("Random Key:", random_key)
    encrypt_text = vernam_encrypt(plain_text, key)
    print("Encrypt Text:", encrypt_text)
    decrypted_text = vernam_decrypt(encrypt_text, key)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
