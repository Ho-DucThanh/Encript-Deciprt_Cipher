alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_to_index = dict(zip(alphabet, range(len(alphabet)))) # Dùng để chuyển letter qua index tướng ứng 
index_to_letter = dict(zip(range(len(alphabet)), alphabet)) # Dùng để chuyển index qua letter tướng ứng 

letter_to_index1 = dict(zip(alphabet1, range(len(alphabet1)))) # Dùng để chuyển letter qua index tướng ứng 
index_to_letter1 = dict(zip(range(len(alphabet1)), alphabet1)) # Dùng để chuyển index qua letter tướng ứng 

def encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i: i + len(key)] for i in range(0, len(message), len(key))
    ]
    print(split_message)
    # Khóa k chạy hết 1 vòng text của nó sẽ quay lại từ đầu cho đến khi = message length

    for each_split in split_message:  # each_split: là những chuỗi của mảng split_message
        i = 0  # Duyệt qua từng kí tự của khóa, kết thúc thì lặp lại i = 0
        for letter in each_split:
            # Duyệt qua các kí tự của từng chuỗi each_split
            number = (letter_to_index[letter] +
                      letter_to_index[key[i]]) % len(alphabet)
            # chuyển letter của mess và key qua index sau đó cộng lại rồi chia dư 26 
            encrypted += index_to_letter[number] # Chuyển lại index qua letter
            i += 1
    return encrypted


def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i: i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] -
                      letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted


def main():
    
    
    message = input("Nhập P: " )
    key = input("Nhập key: " )
    
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print("Giải mã: " + encrypted_message)
    print("Mã hóa: " + decrypted_message)


if __name__ == "__main__":
    main()
