def giai_ma(text, k):
    plainText = ""
    for i in text:
        if i.isalpha():  # nếu i là chữ cái
            shift = 26 - (k % 26) # đảm bảo shift > 0
            if i.isupper():  # i là chữ in hoa
                result = chr((ord(i) - 65 - shift) % 26 + 65)  # chr converted số sang chữ từ bảng mã ascii, ord converted chữ sang số
            else:
                result = chr((ord(i) - 97 - shift) % 26 + 97) 
            plainText += result
        else:
            plainText += i
    return plainText


def ma_hoa(text, k):
    cipherText = ""
    for i in text:
        if i.isalpha():
            shift = 26 - (k % 26)
            if i.isupper():
                result = chr((ord(i) - 65 + shift) % 26 + 65)
            else:
                result = chr((ord(i) - 97 + shift) % 26 + 97)
            cipherText += result
        else:
            cipherText += i
    return cipherText


def main():
    text = input("Enter the PlainText: ")

    print("--Mã hóa--")
    for i in range(1, 26):
        encrypt_Text = giai_ma(text, i)
        print(encrypt_Text, " ", i)

    print("--Giải mã--")
    for i in range(1, 26):
        decrypt_text = ma_hoa(text, i)
        print(decrypt_text, " ", i)

if __name__ == "__main__":
    main()
